# -*- coding: utf-8 -*-
__author__ = 'Miguel Freire Couy'
__credits__ = ['Miguel Freire Couy']
__maintainer__ = 'Miguel Freire Couy'
__email__ = 'miguel.couy@outlook.com'
__status__ = 'Production'

import os
import datetime as dt
from dateutil.relativedelta import relativedelta
from pathlib import Path
from typing import Literal, Optional
import pandas as pd
from urllib.error import HTTPError

from settings import settings

SCRIPT_NAME = os.path.basename(__file__)
SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_RUN = dt.datetime.now().strftime('%Y-%m-%d %Hh%Mm%Ss')
SCRIPT_CONFIG: dict = settings
GLOBAL_CONFIG: dict = SCRIPT_CONFIG['global_config']

BASE_URL = 'https://ons-aws-prod-opendata.s3.amazonaws.com/'



ACCEPT_MATTERS = Literal['ENA', 'EAR']
ACCEPT_ITEMS = Literal['Reservatorio', 'Bacia', 'Subsistema', 'REE']


def set_years(date_from: dt.datetime, date_to: dt.datetime) -> list[int]:
    """
    Generates a list of years between two datetime objects inclusive of both 
    start and end years.

    Args:
    - date_from (dt.datetime): The start date from which to begin the year 
      calculation.
    - date_to (dt.datetime): The end date until which to calculate the years.

    Returns:
    - list[int]: A list of years as integers, from the year of date_from to the 
      year of date_to, inclusive.

    Example:
    - If date_from is January 1, 2015 and date_to is December 31, 2020,
      the function will return [2015, 2016, 2017, 2018, 2019, 2020].
    """

    years = range(date_from.year, date_to.year + 1)

    return years

def set_urls(endpoint: str, filename: str, years: list[int]) -> list[str]:
    """
    Constructs a list of complete URLs by appending each year in the given range
    to the base filename, formatted to include the year at the designated
    placeholder.

    Args:
    - endpoint (str): The endpoint part of the URL to which the filename will be
      appended.
    - filename (str): The filename pattern containing a placeholder for the 
      year ('<%Y>'). This placeholder will be replaced by each year in the 
      'years' list.
    - years (list[int]): A list of integer years for which URLs need to be 
      generated.

    Returns:
    - list[str]: A list of fully constructed URLs, each corresponding to a 
      specific year in the 'years' list.

    Example:
    - endpoint = 'dataset/ena_reservatorio_di/'
    - filename = 'report_<%Y>.csv'
    - years = [2019, 2020, 2021]
    The function will return:
    ['https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/ena_reservatorio_di/ENA_DIARIO_RESERVATORIOS_2019.csv',
     'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/ena_reservatorio_di/ENA_DIARIO_RESERVATORIOS_2020.csv',
     'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/ena_reservatorio_di/ENA_DIARIO_RESERVATORIOS_2021.csv']
    """
        
    urls = [
        BASE_URL + endpoint + filename.replace('<%Y>', str(year))
        for year in years
    ]

    return urls

def fetch_data(url: str, not_found_ok: bool = True) -> pd.DataFrame:
    """
    Attempts to fetch data from the given URL and load it into a DataFrame. 
    If the data cannot be found and 'not_found_ok' is set to True, an empty 
    DataFrame is returned. If 'not_found_ok' is False and the data is not found,
    None is returned.

    Args:
    - url (str): The URL from which to fetch the CSV data.
    - not_found_ok (bool): A flag to determine the function's behavior when the
      HTTP request fails due to the data not being found. If True, returns an 
      empty DataFrame; if False, returns None.

    Returns:
    - pd.DataFrame: A DataFrame containing the data fetched from the 
      URL, an empty DataFrame if the data is not found and 'not_found_ok' is
      True, or None if the data is not found and 'not_found_ok' is False.

    Raises:
    - HTTPError: An error exception raised during unsuccessful HTTP requests
      which are not handled by the 'not_found_ok' parameter.
    """

    try:
        return pd.read_csv(
            filepath_or_buffer = url,
            sep = GLOBAL_CONFIG['sep'],
            decimal = GLOBAL_CONFIG['decimal'],
            encoding = GLOBAL_CONFIG['encoding'],
            date_format = GLOBAL_CONFIG['date_format']
        )
    
    except HTTPError:
        if not_found_ok:
            return pd.DataFrame()
        else:
            return None

def get_data(config: Optional[dict] = None,
             matter: Optional[ACCEPT_MATTERS] = None,
             item: Optional[ACCEPT_ITEMS] = None,
             years: Optional[list[int]] = None,
             date_from: Optional[dt.datetime] = None,
             date_to: Optional[dt.datetime] = None,
             not_found_ok: bool = True,
             ) -> pd.DataFrame:
    """
    Retrieves and aggregates data over a series of years from specified URLs
    based on the provided configuration. This function supports fetching data
    either directly via a specified configuration or through a category and item
    specification which maps to a configuration.

    Args:
    - config (Optional[Dict]): Configuration dictionary specifying 'endpoint' 
      and 'filename' directly. This parameter is not needed if 'matter' and 
      'item' are provided.
    - matter (Optional[str]): Category of data, used to derive 'config' if not
      directly provided.
    - item (Optional[str]): Specific item within the 'matter' category, used to
      derive 'config'.
    - years (Optional[List[int]]): List of years for which to fetch the data. If
      not provided, it will derive the years from 'date_from' and 'date_to'.
    - date_from (Optional[dt.datetime]): Start date for the data retrieval. Used
      to compute 'years' if not provided.
    - date_to (Optional[dt.datetime]): End date for the data retrieval. Also
      used to compute 'years'.
    - not_found_ok (bool): If True, missing data for a URL returns an empty
      DataFrame. If False, raises an HTTPError when data for a URL is not found.

    Returns:
    - pd.DataFrame: A DataFrame aggregating all fetched data across the
      specified years. If no data is found and 'not_found_ok' is True, returns
      an empty DataFrame.

    Raises:
    - ValueError: If neither 'config' nor both 'matter' and 'item' are provided.
    - HTTPError: If data for a URL cannot be fetched and 'not_found_ok' is False.

    Example:
    - To fetch data for 'Reservatorio' matter of type 'ENA' for years 2019 to
      2021:
      df = get_data(matter='ENA', item='Reservatorio', years=[2019, 2020, 2021])
    """

    if config is None:
        if matter and item:
            config = SCRIPT_CONFIG['data_config'][matter][item]
        else: 
            raise ValueError(
                'No config parameter provided.'
            )
    
    if years is None:
        if date_from is None and date_to is None:
            date_to = dt.datetime.now()
            date_from = dt.datetime.now() - relativedelta(years = 5)

        years = set_years(
            date_from = date_from,
            date_to = date_to
        )

    urls = set_urls(
        endpoint = config['endpoint'],
        filename = config['filename'],
        years = years
    )
    
    final_df = pd.DataFrame()
    for url in urls:
        url_df = fetch_data(url, not_found_ok)

        final_df = pd.concat(
            objs = [final_df, url_df], 
            ignore_index = True
        )

    return final_df

def etl_data(dataframe: pd.DataFrame, 
             config: dict,
             key_value: Optional[list[str]] = None, 
             date_from: Optional[dt.datetime] = None, 
             date_to: Optional[dt.datetime] = None,
             clean_ok: bool = True,
             save_ok: bool = False,
             save_where: Optional[Path] = None
             ) -> pd.DataFrame:
    """
    Cleans and saves a DataFrame based on specified parameters and configuration.

    This function handles ETL (Extract, Transform, Load) operations on a 
    given DataFrame, such as cleaning the data by filtering and formatting, 
    and saving it to a specified location.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame to be processed.
    - config (dict): Configuration dictionary containing key settings for 
      cleaning and saving the data. It should include:
        - 'key_col' (str): The column name to filter the key values.
        - 'date_col' (str): The column name for date filtering.
        - 'use_col' (List[str]): The list of column names to retain.
        - 'df_name' (str): The name of the resulting CSV file.
    - key_value (Optional[List[str]]): List of key values to filter the 
      DataFrame by. If None, no key-based filtering is applied.
    - date_from (Optional[dt.datetime]): Start date for date range filtering. 
      If None, no start date filtering is applied.
    - date_to (Optional[dt.datetime]): End date for date range filtering. 
      If None, no end date filtering is applied.
    - clean_ok (bool): Flag to indicate if cleaning is required. Defaults to True.
    - save_ok (bool): Flag to indicate if saving is required. Defaults to False.
    - save_where (Optional[Path]): Directory to save the file. If None, saves 
      to a default 'data' directory.

    Returns:
    - pd.DataFrame: The cleaned and/or saved DataFrame.
    """
    def clean_data(dataframe: pd.DataFrame,
                   config: dict, 
                   key_value: Optional[list[str]] = None, 
                   date_from: Optional[dt.datetime] = None, 
                   date_to: Optional[dt.datetime] = None
                   ) -> pd.DataFrame:
        """
        Cleans the given DataFrame by filtering and formatting.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to be cleaned.
        - config (dict): Configuration dictionary containing key settings 
          for cleaning the data.
        - key_value (Optional[List[str]]): List of key values to filter 
          the DataFrame by.
        - date_from (Optional[dt.datetime]): Start date for date range 
          filtering.
        - date_to (Optional[dt.datetime]): End date for date range filtering.

        Returns:
        - pd.DataFrame: The cleaned DataFrame.
        """

        key_col: str = config['key_col']
        date_col: str = config['date_col']
        use_cols: list[str] = config['use_col']
        date_format = GLOBAL_CONFIG['date_format']
        round_float = GLOBAL_CONFIG['round_float']

        if key_value:
            dataframe = dataframe.loc[
                dataframe[key_col].isin(key_value)
            ]
            
        if date_from and date_to:
            dataframe[date_col] = pd.to_datetime(
                arg = dataframe[date_col], 
                format = date_format
            )

            dataframe = dataframe.loc[
                (dataframe[date_col] >= date_from)
                &
                (dataframe[date_col] <= date_to)
            ]

        dataframe = dataframe[use_cols]
        dataframe = dataframe.round(round_float)
        dataframe.reset_index(inplace = True, drop = True) 
        
        return dataframe

    def save_data(dataframe: pd.DataFrame,
                config: dict,
                save_where: Optional[Path] = None
                ) -> pd.DataFrame:
        """
        Saves the given DataFrame to a specified location.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to be saved.
        - config (dict): Configuration dictionary containing key settings 
          for saving the data.
        - save_where (Optional[Path]): Directory to save the file.

        Returns:
        - pd.DataFrame: The saved DataFrame.
        """

        save_path = save_where if save_where else Path(SCRIPT_DIR, 'data')
        
        os.makedirs(
            name = save_path,
            exist_ok = True
        )

        filepath = Path(save_path, config['df_name'])

        dataframe.to_csv(
            path_or_buf = filepath,
            index = False,
            sep = GLOBAL_CONFIG['sep'],
            decimal = GLOBAL_CONFIG['decimal'],
            encoding = GLOBAL_CONFIG['encoding'],
            date_format = GLOBAL_CONFIG['date_format']
        )

        return dataframe

    if clean_ok:
        dataframe = clean_data(dataframe = dataframe,
                               config = config,
                               key_value = key_value,
                               date_from = date_from,
                               date_to = date_to
                               )

    if save_ok:
        dataframe = save_data(dataframe = dataframe,
                              config = config,
                              save_where = save_where
                              )

    return dataframe

def get_ena_by_reservatorio(reservatorios: Optional[list[str]] = None,
                            date_from: Optional[dt.datetime] = None,
                            date_to: Optional[dt.datetime] = None,
                            not_found_ok: bool = True, 
                            clean_ok: bool = True,
                            save_ok: bool = False,
                            save_where: Optional[Path] = None
                            ) -> pd.DataFrame:

    config = SCRIPT_CONFIG['data_config']['ENA']['Reservatorio']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError

    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = reservatorios,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe

def get_ena_by_subsistema(subsistemas: Optional[list[str]] = None,
                          date_from: Optional[dt.datetime] = None,
                          date_to: Optional[dt.datetime] = None,
                          not_found_ok: bool = True, 
                          clean_ok: bool = True,
                          save_ok: bool = False,
                          save_where: Optional[Path] = None
                          ) -> pd.DataFrame:

    config = SCRIPT_CONFIG['data_config']['ENA']['Subsistema']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError

    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = subsistemas,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe

def get_ena_by_bacia(bacias: Optional[list[str]] = None, 
                     date_from: Optional[dt.datetime] = None,
                     date_to: Optional[dt.datetime] = None,
                     not_found_ok: bool = True, 
                     clean_ok: bool = True,
                     save_ok: bool = False,
                     save_where: Optional[Path] = None
                     ) -> pd.DataFrame:
    
    config = SCRIPT_CONFIG['data_config']['ENA']['Bacia']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError

    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = bacias,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe

def get_ena_by_ree(rees: Optional[list[str]] = None, 
                   date_from: Optional[dt.datetime] = None,
                   date_to: Optional[dt.datetime] = None,
                   not_found_ok: bool = True, 
                   clean_ok: bool = True,
                   save_ok: bool = False,
                   save_where: Optional[Path] = None
                   ) -> pd.DataFrame:
    
    config = SCRIPT_CONFIG['data_config']['ENA']['REE']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError
    
    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = rees,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe

def get_ear_by_reservatorio(reservatorios: Optional[list[str]] = None,
                            date_from: Optional[dt.datetime] = None,
                            date_to: Optional[dt.datetime] = None,
                            not_found_ok: bool = True, 
                            clean_ok: bool = True,
                            save_ok: bool = False,
                            save_where: Optional[Path] = None
                            ) -> pd.DataFrame:

    config = SCRIPT_CONFIG['data_config']['EAR']['Reservatorio']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError
    
    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = reservatorios,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe
    
def get_ear_by_subsistema(subsistemas: Optional[list[str]] = None,
                          date_from: Optional[dt.datetime] = None,
                          date_to: Optional[dt.datetime] = None,
                          not_found_ok: bool = True, 
                          clean_ok: bool = True,
                          save_ok: bool = False,
                          save_where: Optional[Path] = None
                          ) -> pd.DataFrame:

    config = SCRIPT_CONFIG['data_config']['EAR']['Subsistema']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError
    
    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = subsistemas,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe

def get_ear_by_bacia(bacias: Optional[list[str]] = None, 
                     date_from: Optional[dt.datetime] = None,
                     date_to: Optional[dt.datetime] = None,
                     not_found_ok: bool = True, 
                     clean_ok: bool = True,
                     save_ok: bool = False,
                     save_where: Optional[Path] = None
                     ) -> pd.DataFrame:
    
    config = SCRIPT_CONFIG['data_config']['EAR']['Bacia']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError

    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = bacias,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe

def get_ear_by_ree(rees: Optional[list[str]] = None, 
                   date_from: Optional[dt.datetime] = None,
                   date_to: Optional[dt.datetime] = None,
                   not_found_ok: bool = True, 
                   clean_ok: bool = True,
                   save_ok: bool = False,
                   save_where: Optional[Path] = None
                   ) -> pd.DataFrame:
    
    config = SCRIPT_CONFIG['data_config']['EAR']['REE']

    dataframe = get_data(
        config = config,
        date_from = date_from,
        date_to = date_to,
        not_found_ok = not_found_ok
    )

    if dataframe.empty: raise pd.errors.EmptyDataError

    dataframe = etl_data(
        dataframe = dataframe,
        config = config,
        key_value = rees,
        date_from = date_from,
        date_to = date_to,
        clean_ok = clean_ok,
        save_ok = save_ok,
        save_where = save_where
    )

    return dataframe


if __name__ == '__main__':
    get_ear_by_bacia(save_ok = True)
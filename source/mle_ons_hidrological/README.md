# Mercado Livre de Energia - Dados Abertos do ONS: Hidrologia

Este projeto foi desenvolvido para automatizar a extração, transformação e carregamento (ETL) de dados referentes à Energia Natural Afluente (ENA) e Energia Armazenável (EAR) em reservatórios, bacias, subsistemas e REEs (Reservatório Equivalente de Energia) do Operador Nacional do Sistema Elétrico (ONS). A partir dos dados disponíveis publicamente no repositório do ONS, este projeto facilita a recuperação, limpeza e armazenamento dos dados de maneira estruturada.


## Instalação

O pacote mle_ons_hidrological está localizado no [PyPI](www.pypi.org).
Considere utilizar a versão mais recente do Python.
Você consegue instalá-lo via pip.

```bash
  #python3
  pip3 install mle_ons_hidrological
```
    
## Uso/Exemplos

```python
from pathlib import Path
from dateutil.relativedelta import relativedelta
import datetime as dt

import mle_ons_hidrological


my_path = Path('data')

today = dt.datetime.now()
two_years_ago = today - relativedelta(years = 2)

mle_ons_hidrological.get_ena_by_subsistema(
    subsistema = ['Norte'],
    date_from = two_years_ago,
    date_to = today,
    save_ok = True,
    save_where = my_path
)

mle_ons_hidrological.get_ear_by_subsistema(
    subsistema = ['Norte'],
    date_from = two_years_ago,
    date_to = today,
    save_ok = True,
    save_where = my_path
)
```


## Documentação do Código

#### Valores de parâmetros permitidos:
| Parâmetro   | Tipo       | Valores                             |
| :---------- | :--------- | :---------------------------------- |

#### Recuperar dados de energia natural afluente (ENA) por reservatório.
```python
  get_ena_by_reservatorio()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `reservatorios` | `list[str]` | **Opcional**. Lista de reservatórios registrados no SIN. |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia natural afluente (ENA) por subsistema.
```python
  get_ena_by_subsistema()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `subsistemas` | `list[str]` | **Opcional**. Lista de subsistemas registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia natural afluente (ENA) por bacia.
```python
  get_ena_by_bacia()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `bacias` | `list[str]` | **Opcional**. Lista de bacias registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia natural afluente (ENA) por Reservatório Equivalente de Energia (REE).
```python
  get_ena_by_ree()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `rees` | `list[str]` | **Opcional**. Lista de Reservatórios Equivalentes de Energia (REE) registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |


#### Recuperar dados de energia armazenável (EAR) por reservatório.
```python
  get_ear_by_reservatorio()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `reservatorios` | `list[str]` | **Opcional**. Lista de reservatórios registrados no SIN. |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia armazenável (EAR) por subsistema.
```python
  get_ear_by_subsistema()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `subsistemas` | `list[str]` | **Opcional**. Lista de subsistemas registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia armazenável (EAR) por bacia.
```python
  get_ear_by_bacia()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `bacias` | `list[str]` | **Opcional**. Lista de bacias registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia armazenável (EAR) por Reservatório Equivalente de Energia (REE).
```python
  get_ena_by_ree()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `rees` | `list[str]` | **Opcional**. Lista de Reservatórios Equivalentes de Energia (REE) registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |


## Melhorias

- Implementar uma funcionalidade que permita a conversão automática de parâmetros repassados pelo usuário como strings para o formato datetime.

- Adicionar uma funcionalidade que converta automaticamente parâmetros repassados como strings para o formato Path.

- Desenvolver uma funcionalidade que permita ao usuário salvar o DataFrame em outros formatos de arquivo, como parquet ou xlsx, além do formato CSV atual, oferecendo maior versatilidade no armazenamento dos dados.

- Implementar uma funcionalidade que permita ao usuário especificar um nome diferente para o arquivo de dados ao salvar.
## Autores

- [@miguelcouy](https://github.com/miguelcouy)

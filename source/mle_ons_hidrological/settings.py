settings = {
    "global_config": {
        "sep": ";",
        "decimal": ".",
        "encoding": "utf8",
        "date_format": "%Y-%m-%d",
        "round_float": 3 
    },
    
    "data_config": {
        "ENA": {
            "Reservatorio": {
                "endpoint": "dataset/ena_reservatorio_di/",
                "filename": "ENA_DIARIO_RESERVATORIOS_<%Y>.csv",
                "df_name": "ena_diario_reservatorios.csv",
                "key_col": "nom_reservatorio",
                "date_col": "ena_data",
                "use_col": [
                    "nom_reservatorio",
                    "cod_resplanejamento",
                    "tip_reservatorio",
                    "nom_bacia",
                    "nom_ree",
                    "id_subsistema",
                    "ena_data",
                    "ena_armazenavel_res_mwmed",
                    "ena_armazenavel_res_percentualmlt",
                    "mlt_ena"
                ]
            },
            "Bacia": {
                "endpoint": "dataset/ena_bacia_di/",
                "filename": "ENA_DIARIO_BACIAS_<%Y>.csv",
                "df_name": "ena_diario_bacias.csv",
                "key_col": "nom_bacia",
                "date_col": "ena_data",
                "use_col": [
                    "nom_bacia",
                    "ena_data",
                    "ena_armazenavel_bacia_mwmed",
                    "ena_armazenavel_bacia_percentualmlt"
                ]
            },
            "Subsistema": {
                "endpoint": "dataset/ena_subsistema_di/",
                "filename": "ENA_DIARIO_SUBSISTEMA_<%Y>.csv",
                "df_name": "ena_diario_subsistema.csv",
                "key_col": "nom_subsistema",
                "date_col": "ena_data",
                "use_col": [
                    "id_subsistema",
                    "nom_subsistema",
                    "ena_data",
                    "ena_armazenavel_regiao_mwmed",
                    "ena_armazenavel_regiao_percentualmlt"
                ]
            },
            "REE": {
                "endpoint": "dataset/ena_ree_di/",
                "filename": "ENA_DIARIO_REE_<%Y>.csv",
                "df_name": "ena_diario_ree.csv",
                "key_col": "nom_reservatorioee",
                "date_col": "ena_data",
                "use_col": [
                    "nom_reservatorioee",
                    "ena_data",
                    "ena_armazenavel_ree_mwmed",
                    "ena_armazenavel_ree_percentualmlt"
                ]
            }
        },
        "EAR": {
            "Reservatorio": {
                "endpoint": "dataset/ear_reservatorio_di/",
                "filename": "EAR_DIARIO_RESERVATORIOS_<%Y>.csv",
                "df_name": "ear_diario_reservatorios.csv",
                "key_col": "nom_reservatorio",
                "date_col": "ear_data",
                "use_col": [
                    "nom_reservatorio",
                    "cod_resplanejamento",
                    "tip_reservatorio",
                    "nom_bacia",
                    "nom_ree",
                    "id_subsistema",
                    "ear_data",
                    "ear_reservatorio_subsistema_proprio_mwmes",
                    "ear_reservatorio_percentual",
                    "ear_total_mwmes"
                ]
            },
            "Bacia": {
                "endpoint": "dataset/ear_bacia_di/",
                "filename": "EAR_DIARIO_BACIAS_<%Y>.csv",
                "df_name": "ear_diario_bacias.csv",
                "key_col": "nomecurto",
                "date_col": "ear_data",
                "use_col": [
                    "nomecurto",
                    "ear_data",
                    "ear_verif_bacia_mwmes",
                    "ear_verif_bacia_percentual"
                ]
            },
            "Subsistema": {
                "endpoint": "dataset/ear_subsistema_di/",
                "filename": "EAR_DIARIO_SUBSISTEMA_<%Y>.csv",
                "df_name": "ear_diario_subsistema.csv",
                "key_col": "id_subsistema",
                "date_col": "ear_data",
                "use_col": [
                    "id_subsistema",
                    "nom_subsistema",
                    "ear_data",
                    "ear_verif_subsistema_mwmes",
                    "ear_verif_subsistema_percentual"
                ]
            },
            "REE": {
                "endpoint": "dataset/ear_ree_di/",
                "filename": "EAR_DIARIO_REE_<%Y>.csv",
                "df_name": "ear_diario_ree.csv",
                "key_col": "nom_ree",
                "date_col": "ear_data",
                "use_col": [
                    "nom_ree",
                    "ear_data",
                    "ear_verif_ree_mwmes",
                    "ear_verif_ree_percentual"
                ]
            }
        }
    }
}
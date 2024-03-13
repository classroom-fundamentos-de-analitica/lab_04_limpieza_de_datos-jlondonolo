"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df = df.replace("-", " ", regex=True).replace("_", " ", regex=True)

    # Limpieza de las columnas "sexo", "tipo_de_emprendimiento" y "barrio"
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["barrio"] = df["barrio"].str.lower()

    # Limpieza de las columnas "idea_negocio" y "línea_crédito"
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.strip()
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip()

    # Conversión a entero de la columna "comuna_ciudadano"
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # Limpieza del formato de la columna "fecha_de_beneficio"
    df["fecha_de_beneficio"] = pd.to_datetime(
        df.fecha_de_beneficio, format="%d/%m/%Y", errors="coerce"
    ).fillna(pd.to_datetime(df.fecha_de_beneficio, format="%Y/%m/%d", errors="coerce"))

    # Limpieza de la columna "monto_del_credito" y conversión a float
    df.monto_del_credito = df.monto_del_credito.str.rstrip()
    df.monto_del_credito = df.monto_del_credito.replace("[,$]", "", regex=True)
    df.monto_del_credito = df.monto_del_credito.replace("(\\.00$)", "", regex=True)
    df.monto_del_credito = df.monto_del_credito.astype(float)

    # Eliminación de columnas duplicadas y valores nulos
    df = df.drop_duplicates().dropna()

    return df

"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import os

    dataframe = pd.read_csv("files/input/solicitudes_de_credito.csv", index_col=0, sep=";")
    dataframe.dropna(axis=0, how="any", inplace=True)

    # Limpieza de las variables
    dataframe["sexo"] = dataframe["sexo"].str.lower()
    dataframe["monto_del_credito"] = (dataframe["monto_del_credito"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float))
    dataframe["fecha_de_beneficio"] = pd.to_datetime(dataframe["fecha_de_beneficio"],dayfirst=True, format="mixed", errors="coerce")

    # Unificación de categorías
    columnas_a_unificar = ["tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]

    for columna in columnas_a_unificar:
        dataframe[columna] = dataframe[columna].str.lower().str.replace(r"[ .-]", "_", regex=True).str.strip()

    dataframe.drop_duplicates(inplace=True)

    # Crear el directorio de salida si no existe
    output_dir = "files/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    dataframe.to_csv("files/output/solicitudes_de_credito.csv", sep=";", header=True, index=False)
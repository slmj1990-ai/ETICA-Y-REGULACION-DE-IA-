
#IMPORTACION Y ENTORNO

#LIBRERIAS

import pandas as pd
import numpy as np
import requests
import time
import matplotlib.pyplot as plt
import seaborn as sns
import os


#FUNCIONES/METODOS USADOS
import
os.listdir()
os.path.exists()
os.makedirs()

#CARGA Y GUARDADO DE DATOS
#Pandas
pd.read_csv()
DataFrame.to_csv()
DataFrame.copy()
DataFrame.head()
DataFrame.info()
DataFrame.shape()

#LIMPIEZA Y PROCESAMIENTO (cleaning.py)

#NORMALIZACION DE COLUMNAS
DataFrame.columns
Series.str.lower()
Series.str.strip()
Series.str.replace()

#LIMPIEZA DE TEXTO
DataFrame.select_dtypes()
Series.str.replace(regex=True)
Series.str.title()

#VALORES NULOS Y DUPLICADOS
DataFrame.dropna()
DataFrame.drop_duplicates()
Series.isna()
Series.notna()

#CONVERSION DE TIPOS
pd.to_numeric()
pd.to_datetime()
Series.astype()

#FILTRADO
Indexación booleana (df[df["col"] > x])
DataFrame.get()

#LIMPIEZA ESPECIFICA POR DOMINIO
#PAISES
Series.replace(dict)
Series.str.title()

#FECHAS
pd.to_datetime(errors="coerce")

#OUTLIERS SIMPLES
Comparaciones lógicas (>=, <=)
DataFrame.loc[]

#ANALISIS EXPLORATORIO 
#ESTADISTICOS
DataFrame.mean()
DataFrame.value_counts()
DataFrame.nunique()
DataFrame.describe()

#AGRUPACIONES
DataFrame.groupby()
GroupBy.size()
GroupBy.agg()
GroupBy.mean()
GroupBy.reset_index()

#INTEGRACION Y UNION DE DATASETS
DataFrame.merge()
how="left" | "inner"
on=
suffixes=()

#APIs (WORLD BANK Y OPENALEX)
#REQUESTS
requests.get()
Response.json()

#MANEJO DE ESTRUCTURAS JSON
.get(key, default)
Comprensiones de listas
Diccionarios anidados

#CONTROL DE EJECUCION
time.sleep()
Condicionales if

#CREACIN DE VARIABLES ANALITICAS
DataFrame.mean(axis=1)
DataFrame.select_dtypes(include="number")

Nuevas columnas por asignación:
df["new_col"] = ...

#VISUALIZACION DE DATOS 
#MATPLOTLI
plt.figure()
plt.xlabel()
plt.ylabel()
plt.title()
plt.show()
plt.text()

#SEABORN
sns.scatterplot()
sns.barplot()
sns.lineplot()

#VALORES
print()
type()
len()
list()

#FUNCIONES PROPIAS CREADAS 
clean_policies()
clean_etica()
normalize_columns()
clean_strings()
remove_duplicates()
drop_fully_null_rows()
clean_countries()
clean_dates()
log_dimensions()


para push
##### LIMPIEZA #####

import pandas as pd
import numpy as np


# FUNCIONES GENERAL

#Igualando nombres de columnas
def normalize_columns(df):
    df = df.copy()
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("\n", "", regex=False)
        .str.replace(r"[()]", "", regex=True)
    )
    return df

#Formato y limpieza: cadenas de texto, strings, duplicados, valores nulos
def clean_strings(df):
    df = df.copy()
    str_cols = df.select_dtypes(include="object").columns

    for col in str_cols:
        df[col] = (
            df[col]
            .str.lower()
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.replace(";", ",")
        )
    return df


def remove_duplicates(df):
    return df.drop_duplicates()


def drop_fully_null_rows(df):
    return df.dropna(how="all")

#Verificando dimensiones 
def log_dimensions(df, label=""):
    print(f"{label} shape: {df.shape}")
    return df


# LIMPIEZA DE PAÍSES


def clean_countries(df):
    df = df.copy()

    country_map = {
        "united states of america": "united states",
        "u.s.a.": "united states",
        "usa": "united states",
        "uk": "united kingdom",
        "russian federation": "russia",
        "republic of korea": "south korea"
    }

    if "country" in df.columns:
        df["country"] = (
            df["country"]
            .replace(country_map)
            .str.title()
        )

    return df



# Formato y limpieza de fechas

def clean_dates(df, date_columns):
    df = df.copy()
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df



# LIMPIEZA DATASET POLICIES


def clean_policies(df):
    df = df.copy()
    df = log_dimensions(df, "Raw policies")

    df = normalize_columns(df)
    df = clean_strings(df)
    df = remove_duplicates(df)
    df = drop_fully_null_rows(df)

    df = clean_dates(df, ["start_date", "end_date", "entered_into_force_on"])

    # Crear año desde deployment_year para unificación con dataset ética 
    if "deployment_year" in df.columns:
        df["year"] = pd.to_numeric(df["deployment_year"], errors="coerce")

    df = df.dropna(subset=["country", "year"])

    # Filtrar años razonables
    df = df[(df["year"] >= 2000) & (df["year"] <= 2030)]
    df["year"] = df["year"].astype(int)

    # Política activa para comparacion VS politicas inactivas 
    if "end_date" in df.columns:
        df["policy_active"] = df["end_date"].isna()

    df = clean_countries(df)

#Selección de columnas clave
    cols_keep = [
        "policy_initiative_id",
        "english_name",
        "country",
        "year",
        "ai_principles",
        "ai_policy_areas",
        "themes",
        "policy_instrument_type",
        "policy_instrument_type_category",
        "policy_active"
    ]

    cols_keep = [c for c in cols_keep if c in df.columns]
    df = df[cols_keep]
#Verificacion de dimenensiones 
    df = log_dimensions(df, "Clean policies")
    return df


# LIMPIEZA DATASET ÉTICA

#Verificaci{on de dimensiones 
def clean_etica(df):
    df = df.copy()
    df = log_dimensions(df, "Raw ética")
#Formato y limpieza: cadenas de texto, strings, duplicados, valores nulos
    df = normalize_columns(df)
    df = clean_strings(df)
    df = remove_duplicates(df)
    df = drop_fully_null_rows(df)

#Seleccionando columnas clave
    cols_keep = [
        "sector",
        "tipo_ia",
        "nivel_autonomia",
        "transparencia",
        "riesgo_sesgo",
        "impacto_social",
        "privacidad_datos",
        "explicabilidad",
        "cumple_normativa",
        "evaluacion_etica"
    ]

    cols_keep = [c for c in cols_keep if c in df.columns]
    df = df[cols_keep]

    df = log_dimensions(df, "Clean ética")
    return df



# BLOQUE SEGURO de investigación y aprendizaje


if __name__ == "__main__":
    print("✔ cleaning.py listo y sin ejecución accidental")


#ESTRUCTURA

#Igualacion y normalizacion de nombres de columnas
#Control de dimensiones
#Eliminación de duplicados
#Eliminación de columnas totalmente nulas
#Limpieza de cadenas de texto (strings): mayuculas a minusculas, espacios y separadores
#Eliminación de filas sin información clave: country, year
#Limpieza de países
#Corrección de países duplicados por nombre
#Formato y limpieza de fechas
#Normalización de valores categóricos
#Control básico de outliers o valores atípicos (años)

#Objetivo: Garantizar consitencia y calidad analítica en los datos 



para push
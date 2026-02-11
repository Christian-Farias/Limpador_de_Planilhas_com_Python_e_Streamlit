import pandas as pd
import re
from unidecode import unidecode

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .map(unidecode)
        .str.replace(r'[^a-z0-9_]+', '_', regex=True)
    )
    return df


def trim_strings(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].astype(str).str.strip()
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def fix_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')
    return df


def remove_nulls(df: pd.DataFrame, strategy='drop') -> pd.DataFrame:
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'zero':
        return df.fillna(0)
    return df
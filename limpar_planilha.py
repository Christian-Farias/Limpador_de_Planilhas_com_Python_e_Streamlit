import streamlit as st
import pandas as pd
from utils_lp import (
    clean_columns, trim_strings, remove_duplicates,
    fix_numeric_columns, remove_nulls
)

st.set_page_config(page_title="Limpeza de Planilhas", layout="wide")

st.title("Limpador de planilhas")

file = st.file_uploader("Upload do arquivo (CSV ou Excel)", type=["csv", "xlsx"])

if file:
    df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)

    st.subheader("Dados originais")
    st.dataframe(df)

    st.sidebar.header("Limpezas")
    if st.sidebar.checkbox("Padronizar nomes das colunas"):
        df = clean_columns(df)

    if st.sidebar.checkbox("Remover espaços em textos"):
        df = trim_strings(df)

    if st.sidebar.checkbox("Remover duplicatas"):
        df = remove_duplicates(df)

    if st.sidebar.checkbox("Corrigir tipos numéricos"):
        df = fix_numeric_columns(df)


    null_strategy = st.sidebar.selectbox(
        "Tratamento de nulos",
        ["Nenhum", "Remover linhas", "Substituir por zero"]
    )

    if null_strategy == "Remover linhas":
        df = remove_nulls(df, "drop")
    elif null_strategy == "Substituir por zero":
        df = remove_nulls(df, "zero")

    st.subheader("Dados limpos")
    st.dataframe(df)

    st.download_button(
        "Baixar planilha limpa",
        df.to_csv(index=False).encode("utf-8"),
        "planilha_limpa.csv",
        "text/csv"
    )
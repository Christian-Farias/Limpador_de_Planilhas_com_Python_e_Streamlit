# Limpador de Planilhas com Python e Streamlit

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas)](https://pandas.pydata.org/)

> Aplicação web interativa para padronização, limpeza e tratamento automático de planilhas CSV.

---
# Preview da Aplicação

<div align="center">
  <img src="assets/preview.png" width="400"/>
</div>

---

## Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Stack Tecnológica](#-stack-tecnológica)
- [Estrutura do Projeto](#-estrutura-do-projeto)

---

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de resolver um problema muito comum no dia a dia de quem trabalha com dados: **planilhas desorganizadas e inconsistentes**.

Com poucos cliques, é possível transformar um arquivo CSV bruto em uma base padronizada, limpa e pronta para análise 

---

## 🚀 Funcionalidades

### 📌 Padronização de Colunas
- Remove acentos  
- Converte para minúsculas  
- Substitui espaços e caracteres especiais por `_`  

### ✂️ Limpeza de Textos
- Remove espaços extras  
- Padroniza campos string  

### 🔁 Remoção de Duplicados
- Elimina registros repetidos automaticamente  

### 🔢 Correção de Tipos Numéricos
- Conversão automática com `pd.to_numeric()`  
- Tratamento de erros  

### 🚫 Tratamento de Valores Nulos
- Remover linhas com nulos  
- Substituir nulos por zero  

### ⬇️ Exportação
- Download da planilha limpa em formato CSV  

---

## 🛠️ Stack Tecnológica

### Core
- **Python 3.10+**
- **Streamlit**
- **Pandas**

### Bibliotecas Auxiliares
- **Unidecode**
- **Regex (re)**

---

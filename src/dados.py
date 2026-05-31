# src/dados.py

"""Carregamento de dados locais (JSON e CSV)."""

import json

import pandas as pd
import streamlit as st

from src.config import (
    CACHE_DADOS_SEGUNDOS,
    PATH_CARTEIRA,
    PATH_HISTORICO,
    PATH_MOEDAS,
    PATH_PERFIL,
)
from src.tipos import MoedaInfo, PerfilCambista


@st.cache_data(ttl=CACHE_DADOS_SEGUNDOS)
def carregar_dados() -> tuple[
    PerfilCambista,
    pd.DataFrame,
    pd.DataFrame,
    list[MoedaInfo],
]:
    """Carrega todos os arquivos de dados necessários para o agente.

    Returns:
        Tupla com perfil, carteira, histórico e moedas disponíveis.
    """
    with open(file=PATH_PERFIL, encoding="utf-8") as arquivo:
        perfil: PerfilCambista = json.load(fp=arquivo)

    carteira: pd.DataFrame = pd.read_csv(
        filepath_or_buffer=PATH_CARTEIRA,
        encoding="utf-8",
    )

    historico: pd.DataFrame = pd.read_csv(
        filepath_or_buffer=PATH_HISTORICO,
        encoding="utf-8",
    )

    with open(file=PATH_MOEDAS, encoding="utf-8") as arquivo:
        moedas: list[MoedaInfo] = json.load(fp=arquivo)

    return perfil, carteira, historico, moedas

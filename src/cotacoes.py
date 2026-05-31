# src/cotacoes.py

"""APIs de cotação em tempo real (AwesomeAPI e CoinGecko)."""

import requests
import streamlit as st

from src.config import CACHE_COTACOES_SEGUNDOS


@st.cache_data(ttl=CACHE_COTACOES_SEGUNDOS)
def cotacao_usd() -> float:
    """Consulta a cotação atual do dólar usando a AwesomeAPI.

    Returns:
        Cotação USD/BRL ou valor de fallback em caso de erro.
    """
    try:
        resposta: requests.Response = requests.get(
            url="https://economia.awesomeapi.com.br/json/last/USD-BRL",
            timeout=10,
        )
        resposta.raise_for_status()
        dados: dict[str, dict[str, str]] = resposta.json()
        return float(dados["USDBRL"]["bid"])
    except (requests.RequestException, KeyError, ValueError):
        return 5.07


@st.cache_data(ttl=CACHE_COTACOES_SEGUNDOS)
def cotacao_eur() -> float:
    """Consulta a cotação atual do euro usando a AwesomeAPI.

    Returns:
        Cotação EUR/BRL ou valor de fallback em caso de erro.
    """
    try:
        resposta: requests.Response = requests.get(
            url="https://economia.awesomeapi.com.br/json/last/EUR-BRL",
            timeout=10,
        )
        resposta.raise_for_status()
        dados: dict[str, dict[str, str]] = resposta.json()
        return float(dados["EURBRL"]["bid"])
    except (requests.RequestException, KeyError, ValueError):
        return 5.48


@st.cache_data(ttl=CACHE_COTACOES_SEGUNDOS)
def cotacao_btc() -> float:
    """Consulta a cotação atual do bitcoin usando a CoinGecko.

    Returns:
        Cotação BTC/BRL ou valor de fallback em caso de erro.
    """
    try:
        resposta: requests.Response = requests.get(
            url=(
                "https://api.coingecko.com/api/v3/simple/price"
                "?ids=bitcoin&vs_currencies=brl"
            ),
            timeout=10,
        )
        resposta.raise_for_status()
        dados: dict[str, dict[str, float]] = resposta.json()
        return float(dados["bitcoin"]["brl"])
    except (requests.RequestException, KeyError, ValueError):
        return 182350.00

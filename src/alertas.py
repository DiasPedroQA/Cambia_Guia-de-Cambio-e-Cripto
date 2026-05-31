# src/alertas.py

"""Sistema de alertas proativos de variação de cotações."""

import streamlit as st
from src.config import ALERTA_VARIACAO


def _tocar_alerta_sonoro() -> None:
    """Reproduz um som de alerta usando HTML5 Audio."""
    st.markdown(body="""
    <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-09.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)


def verificar_alertas(
    cotacao_dolar: float,
    cotacao_euro: float,
    cotacao_bitcoin: float,
) -> list[str]:
    """Verifica variações significativas nas cotações e retorna alertas.

    Args:
        cotacao_dolar: Cotação atual do dólar.
        cotacao_euro: Cotação atual do euro.
        cotacao_bitcoin: Cotação atual do bitcoin.

    Returns:
        Lista de strings com alertas de variação.
    """
    alertas: list[str] = []
    teve_alerta = False  # NOVA variável

    if "ultima_cotacao_usd" in st.session_state:
        valor_anterior: float = float(st.session_state.ultima_cotacao_usd)
        if valor_anterior != 0:
            variacao: float = (
                (cotacao_dolar - valor_anterior) / valor_anterior
            ) * 100
            if abs(variacao) > ALERTA_VARIACAO:
                alertas.append(
                    f"⚠️ Dólar variou {variacao:+.2f}% "
                    f"e está R$ {cotacao_dolar:.2f}"
                )
                teve_alerta = True  # NOVA linha

    if "ultima_cotacao_btc" in st.session_state:
        valor_anterior_btc: float = float(st.session_state.ultima_cotacao_btc)
        if valor_anterior_btc != 0:
            variacao_btc: float = (
                (cotacao_bitcoin - valor_anterior_btc) / valor_anterior_btc
            ) * 100
            if abs(variacao_btc) > ALERTA_VARIACAO:
                alertas.append(
                    f"⚠️ Bitcoin variou {variacao_btc:+.2f}% "
                    f"e está R$ {cotacao_bitcoin:,.2f}"
                )
                teve_alerta = True  # NOVA linha

    st.session_state.ultima_cotacao_usd = cotacao_dolar
    st.session_state.ultima_cotacao_eur = cotacao_euro
    st.session_state.ultima_cotacao_btc = cotacao_bitcoin

    # Tocar som se houver alerta (NOVO)
    if teve_alerta:
        _tocar_alerta_sonoro()

    return alertas

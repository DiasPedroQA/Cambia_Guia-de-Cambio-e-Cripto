# src/ui/badges.py

"""Badges e indicadores visuais de status do mercado."""

from datetime import datetime

import streamlit as st


def renderizar_status_mercado(usd: float, eur: float, btc: float) -> None:
    """Renderiza badges indicando o status do mercado.

    Args:
        usd: Cotação atual do dólar (USD/BRL).
        eur: Cotação atual do euro (EUR/BRL).
        btc: Cotação atual do bitcoin (BTC/BRL).
    """
    # Obter hora atual (import no topo do arquivo)
    hora_atual: int = datetime.now().hour

    # Criar colunas para os badges
    coluna_dolar, coluna_euro, coluna_btc, coluna_mercado = st.columns(4)

    # ============ BADGE DÓLAR ============
    with coluna_dolar:
        if usd > 5.20:
            st.error(body="🔴 Dólar ALTO")
        elif usd > 5.00:
            st.warning(body="🟡 Dólar MÉDIO")
        else:
            st.success(body="🟢 Dólar BAIXO")

    # ============ BADGE EURO ============
    with coluna_euro:
        if eur > 5.70:
            st.error(body="🔴 Euro ALTO")
        elif eur > 5.40:
            st.warning(body="🟡 Euro MÉDIO")
        else:
            st.success(body="🟢 Euro BAIXO")

    # ============ BADGE BITCOIN ============
    with coluna_btc:
        if btc > 200_000:
            st.error(body="🔴 BTC Aquecido")
        elif btc > 180_000:
            st.warning(body="🟡 BTC Estável")
        else:
            st.success(body="🟢 BTC Oportunidade")

    # ============ BADGE STATUS DO MERCADO ============
    with coluna_mercado:
        # Verificar se é dia útil e horário comercial
        dia_semana: int = datetime.now().weekday()  # Semana: 0 = Segunda, 6 = Domingo
        eh_dia_util: bool = dia_semana < 5  # Seg-Sex
        eh_horario_comercial: bool = 10 <= hora_atual < 17

        if eh_dia_util and eh_horario_comercial:
            st.info(body="🏦 Mercado ABERTO")
        elif eh_dia_util:
            st.warning(body="🌅 Fora do horário")
        else:
            st.caption(body="🌙 Mercado FECHADO")

# src/ui/graficos.py

"""Componentes de gráficos para visualização de cotações."""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random


def gerar_historico_simulado(cotacao_atual: float, horas: int = 24) -> pd.DataFrame:
    """Gera um histórico simulado de cotações para o gráfico.
    
    Args:
        cotacao_atual: Valor atual da cotação.
        horas: Número de horas para simular.
        
    Returns:
        DataFrame com timestamps e valores simulados.
    """
    agora: datetime = datetime.now()
    dados: list[dict] = []

    for i in range(horas, -1, -1):
        timestamp: datetime = agora - timedelta(hours=i)
        # Simula variação de ±1% em torno do valor atual
        variacao: float = random.uniform(a=-0.01, b=0.01)
        valor: float = cotacao_atual * (1 + variacao)
        dados.append({
            "timestamp": timestamp,
            "valor": valor,
        })

    return pd.DataFrame(dados)


def renderizar_grafico_cotacao(
    moeda: str,
    cotacao_atual: float,
    horas: int = 24,
) -> None:
    """Renderiza um mini-gráfico de linha com a evolução da cotação.
    
    Args:
        moeda: Nome da moeda (USD, EUR, BTC).
        cotacao_atual: Valor atual da cotação.
        horas: Período do histórico em horas.
    """
    emojis: dict[str, str] = {"USD": "💵", "EUR": "💶", "BTC": "₿"}
    emoji: str = emojis.get(moeda, "📊")

    historico: pd.DataFrame = gerar_historico_simulado(cotacao_atual=cotacao_atual, horas=horas)

    st.subheader(body=f"{emoji} {moeda} - Últimas {horas}h")

    # Gráfico de linha minimalista
    st.line_chart(
        data=historico,
        x="timestamp",
        y="valor",
        height=150,
    )

    # Indicador de tendência
    primeiro: float = historico["valor"].iloc[0]
    ultimo: float = historico["valor"].iloc[-1]
    variacao: float = ((ultimo - primeiro) / primeiro) * 100

    if variacao > 0:
        st.success(body=f"📈 +{variacao:.2f}% no período")
    elif variacao < 0:
        st.error(body=f"📉 {variacao:.2f}% no período")
    else:
        st.info(body="➡️ Estável no período")

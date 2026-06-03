# app.py

"""Câmbia - Seu Guia de Câmbio e Cripto.

Ponto de entrada principal da aplicação Streamlit.
"""

import streamlit as st

from src.alertas import verificar_alertas
from src.cotacoes import cotacao_btc, cotacao_eur, cotacao_usd
from src.dados import carregar_dados
from src.ui.badges import renderizar_status_mercado
from src.ui.chat import renderizar_chat
from src.ui.estilos import aplicar_estilos
from src.ui.sidebar import renderizar_sidebar


def main() -> None:
    """Função principal que renderiza a interface completa do Streamlit."""
    st.set_page_config(
        page_title="Câmbia - Guia de Câmbio",
        page_icon="💱",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Aplicar CSS personalizado
    aplicar_estilos()

    st.title(body="💱 Câmbia - Seu Guia de Câmbio e Cripto")
    st.caption(
        body="Seu assistente pessoal para acompanhar moedas e criptomoedas"
    )

    # Carregar dados
    perfil, carteira, _, _ = carregar_dados()

    # Obter cotações
    usd_atual: float = cotacao_usd()
    eur_atual: float = cotacao_eur()
    btc_atual: float = cotacao_btc()

    # NOVO: Status do mercado
    renderizar_status_mercado(usd=usd_atual, eur=eur_atual, btc=btc_atual)

    # Renderizar componentes
    renderizar_sidebar(perfil=perfil, usd=usd_atual,
                       eur=eur_atual, btc=btc_atual)

    alertas_gerados: list[str] = verificar_alertas(
        cotacao_dolar=usd_atual,
        cotacao_euro=eur_atual,
        cotacao_bitcoin=btc_atual,
    )
    for alerta in alertas_gerados:
        st.warning(body=alerta)

    renderizar_chat(perfil=perfil, carteira=carteira)


if __name__ == "__main__":
    main()

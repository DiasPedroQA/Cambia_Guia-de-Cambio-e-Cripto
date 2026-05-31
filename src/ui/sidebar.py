# src/sidebar.py

"""Componente da barra lateral com cotações e perfil."""

import streamlit as st

from src.tipos import MetaAcumulacao, PerfilCambista


def renderizar_sidebar(
    perfil: PerfilCambista,
    usd: float,
    eur: float,
    btc: float,
) -> None:
    """Renderiza a barra lateral com cotações e perfil do usuário.

    Args:
        perfil: Dados do perfil do cambista.
        usd: Cotação atual do dólar.
        eur: Cotação atual do euro.
        btc: Cotação atual do bitcoin.
    """
    with st.sidebar:
        st.header(body="📊 Cotações em Tempo Real")

        coluna1, coluna2, coluna3 = st.columns(3)
        with coluna1:
            st.metric(label="💵 Dólar", value=f"R$ {usd:.2f}")
        with coluna2:
            st.metric(label="💶 Euro", value=f"R$ {eur:.2f}")
        with coluna3:
            st.metric(label="₿ Bitcoin", value=f"R$ {btc:,.0f}")

        st.divider()

        st.header(body="👤 Seu Perfil")
        st.write(f"**Cliente:** {perfil['nome']}")
        st.write(f"**Perfil:** {perfil['perfil_cambio']}")

        if "profissao" in perfil:
            st.write(f"**Profissão:** {perfil['profissao']}")
        if "renda_mensal" in perfil:
            st.write(f"**Renda Mensal:** R$ {perfil['renda_mensal']:,.2f}")

        st.subheader(body="Sua Carteira")
        st.write(f"💵 USD: ${perfil['saldo_usd']:,.2f}")
        st.write(f"💶 EUR: €{perfil['saldo_eur']:,.2f}")
        st.write(f"₿ BTC: {perfil['saldo_btc']:.6f}")

        if "meta_acumulacao" in perfil:
            meta: MetaAcumulacao = perfil["meta_acumulacao"]
            st.divider()
            st.subheader(body="🎯 Meta")
            st.write(
                f"Acumular {meta['moeda']} {meta['valor_alvo']:,.2f} "
                f"até {meta['prazo']}"
            )

        st.divider()
        st.caption(body="📡 Fontes: AwesomeAPI | CoinGecko")
        st.caption(body="⚡ Atualização em tempo real")

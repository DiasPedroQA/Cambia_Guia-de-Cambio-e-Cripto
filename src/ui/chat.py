# src/ui/chat.py

"""Componente do chat interativo."""

import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from src.ollama_cliente import perguntar
from src.prompts import SYSTEM_PROMPT, montar_contexto
from src.tipos import PerfilCambista


def _renderizar_sugestoes() -> str | None:
    """Renderiza botões com perguntas sugeridas para o usuário.

    Returns:
        Texto da pergunta selecionada ou None se nenhuma for clicada.
    """
    st.caption(body="💡 Perguntas sugeridas:")

    sugestoes: list[str] = [
        "💰 Qual o valor total da minha carteira?",
        "📊 Como está o dólar hoje?",
        "₿ Vale a pena comprar bitcoin agora?",
        "💱 Qual a diferença entre dólar e euro?",
        "📈 Como está meu patrimônio?",
    ]

    colunas: list[DeltaGenerator] = st.columns(len(sugestoes))
    pergunta_selecionada: str | None = None

    for i, sugestao in enumerate(iterable=sugestoes):
        with colunas[i]:
            if st.button(
                label=sugestao,
                key=f"sugestao_{i}",
                use_container_width=True,
            ):
                pergunta_selecionada = sugestao

    return pergunta_selecionada


def _processar_pergunta(
    perfil: PerfilCambista,
    carteira: pd.DataFrame,
    pergunta: str,
) -> None:
    """Processa a pergunta do usuário e adiciona ao histórico.

    Args:
        perfil: Dados do perfil do cambista.
        carteira: DataFrame com histórico de operações.
        pergunta: Texto da pergunta do usuário.
    """
    # Adicionar pergunta ao histórico
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta,
    })

    with st.chat_message(name="user"):
        st.write(pergunta)

    # Gerar resposta do agente
    with st.spinner(
        text="💭 Consultando cotações e processando sua pergunta..."
    ):
        prompt_completo: str = f"""{SYSTEM_PROMPT}

CONTEXTO DA CLIENTE:
{montar_contexto(perfil=perfil, carteira=carteira)}

Pergunta: {pergunta}"""

        resposta_agente: str = perguntar(prompt_completo=prompt_completo)

        st.session_state.mensagens.append({
            "role": "assistant",
            "content": resposta_agente,
        })

        with st.chat_message(name="assistant"):
            st.write(resposta_agente)


def renderizar_chat(perfil: PerfilCambista, carteira: pd.DataFrame) -> None:
    """Renderiza o histórico do chat e processa novas mensagens.

    Args:
        perfil: Dados do perfil do cambista.
        carteira: DataFrame com histórico de operações.
    """
    # Inicializar histórico de mensagens
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    # Exibir histórico do chat
    for mensagem in st.session_state.mensagens:
        with st.chat_message(name=mensagem["role"]):
            st.write(mensagem["content"])

    # Sugestões rápidas
    pergunta_sugerida: str | None = _renderizar_sugestoes()

    # Input do usuário
    pergunta: str | None = st.chat_input(
        placeholder=(
            "💬 Pergunte sobre cotações, sua carteira "
            "ou tire dúvidas sobre câmbio..."
        ),
    )

    if pergunta_final := pergunta or pergunta_sugerida:
        _processar_pergunta(
            perfil=perfil,
            carteira=carteira,
            pergunta=pergunta_final,
        )

    # Botão para limpar conversa
    if st.session_state.mensagens:
        st.divider()
        if st.button(
            label="🗑️ Limpar conversa",
            use_container_width=True,
        ):
            st.session_state.mensagens = []
            st.rerun()

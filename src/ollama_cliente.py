# src/ollama_cliente.py

"""Cliente de comunicação com o Ollama."""

import requests

from src.config import MODELO, OLLAMA_URL


def perguntar(prompt_completo: str) -> str:
    """Envia o prompt para o modelo LLM e retorna a resposta.

    Args:
        prompt_completo: Prompt completo com sistema, contexto e pergunta.

    Returns:
        Resposta do modelo ou mensagem de erro.
    """
    try:
        resposta: requests.Response = requests.post(
            url=OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt_completo,
                "stream": False,
            },
            timeout=60,
        )
        resposta.raise_for_status()
        dados_resposta: dict[str, str] = resposta.json()
        return str(dados_resposta["response"])
    except requests.Timeout:
        return "⏰ Ops, demorei demais. Tente de novo!"
    except requests.RequestException as erro:
        return f"❌ Erro ao consultar o modelo: {erro}"

# src/prompts.py

"""System prompt e montagem de contexto para o LLM."""

import pandas as pd

from src.cotacoes import cotacao_btc, cotacao_eur, cotacao_usd
from src.tipos import PerfilCambista

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT: str = """
Você é a Câmbia, uma guia amigável de câmbio e criptomoedas.

OBJETIVO:
Ajudar a cliente a entender cotações, acompanhar sua carteira e aprender sobre moedas.

REGRAS:
- SEMPRE use as cotações reais fornecidas no contexto
- NUNCA recomende comprar ou vender — apenas informe dados e explique cenários
- JAMAIS responda perguntas fora de câmbio/cripto
- Linguagem simples, com toque de humor leve
- Se não souber, admita e ofereça pesquisar junto
- Mostre a fonte das cotações (AwesomeAPI para USD/EUR, CoinGecko para BTC)
- Se houver alerta de variação, mencione-o educadamente
- Responda em no máximo 3 parágrafos
"""


# ============ MONTAR CONTEXTO ============
def montar_contexto(perfil: PerfilCambista, carteira: pd.DataFrame) -> str:
    """Monta o contexto com dados da cliente e cotações em tempo real.

    Args:
        perfil: Dados do perfil do cambista.
        carteira: DataFrame com histórico de operações.

    Returns:
        String formatada com todos os dados para injetar no prompt.
    """
    usd: float = cotacao_usd()
    eur: float = cotacao_eur()
    btc: float = cotacao_btc()

    # Campos obrigatórios - acesso direto sem risco
    saldo_usd: float = perfil["saldo_usd"]
    saldo_eur: float = perfil["saldo_eur"]
    saldo_btc: float = perfil["saldo_btc"]
    patrimonio_brl: float = perfil["patrimonio_total_brl"]

    total_usd_brl: float = saldo_usd * usd
    total_eur_brl: float = saldo_eur * eur
    total_btc_brl: float = saldo_btc * btc
    patrimonio_total: float = (
        patrimonio_brl + total_usd_brl + total_eur_brl + total_btc_brl
    )

    contexto: str = f"""
    CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_cambio']}
    OBJETIVO: {perfil['objetivo_principal']}
    
    CARTEIRA ATUAL (com cotações em tempo real):
    - USD: ${saldo_usd:,.2f} × R$ {usd:.2f} = R$ {total_usd_brl:,.2f}
    - EUR: €{saldo_eur:,.2f} × R$ {eur:.2f} = R$ {total_eur_brl:,.2f}
    - BTC: {saldo_btc:.6f} × R$ {btc:,.2f} = R$ {total_btc_brl:,.2f}
    
    PATRIMÔNIO TOTAL EM BRL: R$ {patrimonio_total:,.2f}
    
    ÚLTIMAS OPERAÇÕES:
    {carteira.tail(n=5).to_string(index=False)}
    
    FONTES: USD/EUR → AwesomeAPI | BTC → CoinGecko
    """
    return contexto

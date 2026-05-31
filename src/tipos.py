# src/tipos.py

"""Tipos personalizados para o agente Câmbia."""

from typing import TypedDict


class MetaAcumulacao(TypedDict):
    """Tipo para meta de acumulação de moeda."""
    moeda: str
    valor_alvo: float
    prazo: str


class PerfilCambistaBase(TypedDict):
    """Campos obrigatórios do perfil do cambista."""
    nome: str
    idade: int
    perfil_cambio: str
    objetivo_principal: str
    patrimonio_total_brl: float
    saldo_usd: float
    saldo_eur: float
    saldo_btc: float


class PerfilCambistaOpcional(TypedDict, total=False):
    """Campos opcionais do perfil do cambista."""
    profissao: str
    renda_mensal: float
    meta_acumulacao: MetaAcumulacao


class PerfilCambista(PerfilCambistaBase, PerfilCambistaOpcional):
    """Tipo completo do perfil do cambista (obrigatório + opcional)."""


class MoedaInfo(TypedDict):
    """Tipo para informações de uma moeda disponível."""
    codigo: str
    nome: str
    tipo: str
    pais: str
    volatilidade: str
    indicado_para: str


class MensagemChat(TypedDict):
    """Tipo para mensagem do histórico de chat."""
    role: str
    content: str

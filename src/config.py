# src/config.py

"""Configurações e constantes do agente Câmbia."""

# ============ CONFIGURAÇÃO OLLAMA ============
OLLAMA_URL: str = "http://localhost:11434/api/generate"
MODELO: str = "llama3.2:1b"

# ============ CONFIGURAÇÃO DE ALERTAS ============
ALERTA_VARIACAO: float = 2.0  # % para disparar alerta

# ============ CONFIGURAÇÃO DE CACHE ============
CACHE_DADOS_SEGUNDOS: int = 300  # 5 minutos
CACHE_COTACOES_SEGUNDOS: int = 60  # 1 minuto

# ============ PATHS DOS ARQUIVOS ============
PATH_PERFIL: str = "./data/perfil_cambista.json"
PATH_CARTEIRA: str = "./data/carteira_moedas.csv"
PATH_HISTORICO: str = "./data/historico_conversas.csv"
PATH_MOEDAS: str = "./data/moedas_disponiveis.json"

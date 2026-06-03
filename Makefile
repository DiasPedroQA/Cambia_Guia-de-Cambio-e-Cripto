# Detecta o comando de Python de forma simples
# Em Windows (CMD/PowerShell) use:  make <alvo>
# Em macOS/Linux use:              make <alvo>

# Tenta usar python, depois python3
PYTHON := $(shell command -v python 2> NUL || command -v python3 2> /dev/null)

# Caminho do arquivo principal do Streamlit
APP := src/app.py

# --------------------------------------------------------------------
# Alvos principais
# --------------------------------------------------------------------

# Instala dependências globais do projeto
install:
	"$(PYTHON)" -m pip install --upgrade pip
	"$(PYTHON)" -m pip install -r [requirements.txt](VALID_FILE)

# Cria e instala dependências em um venv chamado .venv (recomendado)
venv:
	"$(PYTHON)" -m venv .venv
	. [.venv/bin/activate](VALID_FILE) 2>/dev/null || .venv\Scripts\activate && \
	"$(PYTHON)" -m pip install --upgrade pip && \
	"$(PYTHON)" -m pip install -r [requirements.txt](VALID_FILE)

# Roda o app Streamlit (tenta usar o Python do venv se existir)
run:
	if [ -d ".venv" ]; then \
		. [.venv/bin/activate](VALID_FILE) 2>/dev/null || .venv\Scripts\activate; \
		"$(PYTHON)" -m streamlit run $(APP); \
	else \
		"$(PYTHON)" -m streamlit run $(APP); \
	fi

# Atalho: cria venv + instala deps + roda o app
start: install run

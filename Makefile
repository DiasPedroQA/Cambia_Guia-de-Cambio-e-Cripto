# Detecta o comando de Python de forma simples
# Em Windows (CMD/PowerShell) use:  make <alvo>
# Em macOS/Linux use:              make <alvo>

# Detecta o comando Python disponível
PYTHON := $(shell command -v python 2> /dev/null || command -v python3 2> /dev/null)

# Arquivo principal do Streamlit
APP := src/app.py

# Ambiente virtual
VENV := .venv

# --------------------------------------------------------------------
# Cria ambiente virtual e instala dependências
# --------------------------------------------------------------------
install:
	"$(PYTHON)" -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip 2>/dev/null || \
	$(VENV)\Scripts\python.exe -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -r requirements.txt 2>/dev/null || \
	$(VENV)\Scripts\python.exe -m pip install -r requirements.txt

# --------------------------------------------------------------------
# Executa a aplicação Streamlit usando o ambiente virtual
# --------------------------------------------------------------------
run:
	$(VENV)/bin/python -m streamlit run $(APP) 2>/dev/null || \
	$(VENV)\Scripts\python.exe -m streamlit run $(APP)

# --------------------------------------------------------------------
# Instala tudo e executa
# --------------------------------------------------------------------
start: install run

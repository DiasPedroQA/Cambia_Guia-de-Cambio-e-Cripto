# ==========================================================
# Makefile — Câmbia
# ==========================================================
# Uso: make <comando>
# Exemplo: make install && make run
# ==========================================================

APP     := app.py
VENV    := .venv
PYTHON  := python3

# ==========================================================
# Comandos universais (detecta SO automaticamente)
# ==========================================================

install:
	@echo "📦 Criando ambiente virtual e instalando dependências..."
	@if [ -d $(VENV) ]; then \
		echo "⚠️  Ambiente virtual já existe. Use 'make clean' para recriar."; \
	else \
		$(PYTHON) -m venv $(VENV) && \
		. $(VENV)/bin/activate 2>/dev/null || . $(VENV)/Scripts/activate 2>/dev/null; \
		python -m pip install --upgrade pip && \
		python -m pip install -r requirements.txt && \
		echo "✅ Instalação concluída!"; \
	fi

run:
	@echo "🚀 Iniciando a Câmbia..."
	@if [ -f $(VENV)/bin/streamlit ]; then \
		$(VENV)/bin/streamlit run $(APP); \
	elif [ -f $(VENV)/Scripts/streamlit.exe ]; then \
		$(VENV)/Scripts/streamlit.exe run $(APP); \
	else \
		echo "❌ Streamlit não encontrado. Rode 'make install' primeiro."; \
	fi

start: install run
	@echo "✨ Tudo pronto!"

clean:
	@echo "🧹 Removendo ambiente virtual..."
	@rm -rf $(VENV)
	@echo "✅ Limpeza concluída!"

ollama:
	@echo "🦙 Iniciando Ollama..."
	@ollama serve

ollama-pull:
	@echo "📥 Baixando modelo llama3.2:1b..."
	@ollama pull llama3.2:1b
	@echo "✅ Modelo baixado!"

test:
	@echo "🧪 Verificando instalação..."
	@$(PYTHON) --version
	@which streamlit || echo "❌ Streamlit não instalado"
	@which ollama || echo "❌ Ollama não instalado"
	@echo "✅ Verificação concluída!"

help:
	@echo ""
	@echo "💱 Comandos disponíveis — Câmbia"
	@echo "=================================="
	@echo ""
	@echo "  make install      📦 Criar ambiente e instalar dependências"
	@echo "  make run          🚀 Rodar a aplicação"
	@echo "  make start        ⚡ Instalar + Rodar (tudo de uma vez)"
	@echo "  make clean        🧹 Remover ambiente virtual"
	@echo "  make ollama       🦙 Iniciar servidor Ollama"
	@echo "  make ollama-pull  📥 Baixar modelo llama3.2:1b"
	@echo "  make test         🧪 Verificar se tudo está instalado"
	@echo "  make help         ❓ Mostrar esta ajuda"
	@echo ""

.PHONY: install run start clean ollama ollama-pull test help
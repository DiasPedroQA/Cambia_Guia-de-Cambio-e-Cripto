# ==========================================================
# Makefile - Cambia
# ==========================================================

APP := app.py
VENV := .venv

# ==========================================================
# Linux
# ==========================================================

install-linux:
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -r requirements.txt

run-linux:
	$(VENV)/bin/python -m streamlit run $(APP)

start-linux: install-linux run-linux

clean-linux:
	rm -rf $(VENV)

# ==========================================================
# macOS
# ==========================================================

install-mac:
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -r requirements.txt

run-mac:
	$(VENV)/bin/python -m streamlit run $(APP)

start-mac: install-mac run-mac

clean-mac:
	rm -rf $(VENV)

# ==========================================================
# Windows (CMD / PowerShell)
# ==========================================================

install-win:
	python -m venv $(VENV)
	$(VENV)\Scripts\python.exe -m pip install --upgrade pip
	$(VENV)\Scripts\python.exe -m pip install -r requirements.txt

run-win:
	$(VENV)\Scripts\python.exe -m streamlit run $(APP)

start-win: install-win run-win

clean-win:
	rmdir /s /q $(VENV)

# ==========================================================
# Ajuda
# ==========================================================

help:
	@echo ""
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "Linux:"
	@echo "  make install-linux"
	@echo "  make run-linux"
	@echo "  make start-linux"
	@echo "  make clean-linux"
	@echo ""
	@echo "macOS:"
	@echo "  make install-mac"
	@echo "  make run-mac"
	@echo "  make start-mac"
	@echo "  make clean-mac"
	@echo ""
	@echo "Windows:"
	@echo "  make install-win"
	@echo "  make run-win"
	@echo "  make start-win"
	@echo "  make clean-win"
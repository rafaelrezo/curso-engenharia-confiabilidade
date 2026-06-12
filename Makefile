SHELL := /bin/bash

PYTHON ?= python3
VENV ?= .venv
HOST ?= 127.0.0.1
PORT ?= 8001

PIP := $(VENV)/bin/pip
MKDOCS := $(VENV)/bin/mkdocs
PYTHON_BIN := $(VENV)/bin/python
INSTALL_STAMP := $(VENV)/.install.stamp

.PHONY: help venv install run build strict generate check-content clean clean-site clean-venv

help:
	@echo "Comandos disponíveis:"
	@echo "  make install       Cria o venv e instala dependências"
	@echo "  make run           Roda MkDocs em http://$(HOST):$(PORT)"
	@echo "  make build         Gera o site estático em ./site"
	@echo "  make strict        Valida o build em modo estrito"
	@echo "  make generate      Regenera docs a partir do script local"
	@echo "  make check-content Valida o template editorial dos capítulos"
	@echo "  make clean-site    Remove ./site"
	@echo "  make clean-venv    Remove ./.venv"
	@echo "  make clean         Remove ./site e caches Python"
	@echo ""
	@echo "Variáveis úteis:"
	@echo "  make run PORT=8000"
	@echo "  make run HOST=0.0.0.0 PORT=8001"

venv:
	@test -d "$(VENV)" || $(PYTHON) -m venv "$(VENV)"

$(INSTALL_STAMP): requirements.txt | venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@touch "$(INSTALL_STAMP)"

install: $(INSTALL_STAMP)

run: install
	$(MKDOCS) serve -a "$(HOST):$(PORT)"

build: install
	$(MKDOCS) build

strict: install check-content
	$(MKDOCS) build --strict

generate: install
	$(PYTHON_BIN) scripts/generate_docs.py

check-content: install
	$(PYTHON_BIN) scripts/check_content.py

clean: clean-site
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

clean-site:
	rm -rf site

clean-venv:
	rm -rf "$(VENV)"

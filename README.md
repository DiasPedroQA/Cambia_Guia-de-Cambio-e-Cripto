<!-- README.md -->

# 💱 Câmbia - Guia de Câmbio e Cripto

> Agente de IA Generativa que ajuda você a acompanhar cotações de dólar, euro e bitcoin, gerenciar sua carteira de moedas e aprender sobre câmbio de forma simples.

## 💡 O que a Câmbia faz?

- ✅ Mostra cotações em tempo real (USD, EUR, BTC)
- ✅ Exibe sua carteira com valores atualizados
- ✅ Alerta sobre variações acima de 2%
- ✅ Explica conceitos de câmbio e cripto
- ✅ Histórico de operações

**O que NÃO faz:**

- ❌ Não recomenda compra/venda
- ❌ Não realiza transações reais
- ❌ Não substitui consultoria financeira

## 🏗️ Arquitetura

- Interface: Streamlit
- LLM: Ollama (modelo local)
- Cotações: AwesomeAPI (USD/EUR) + CoinGecko (BTC)
- Dados: JSON/CSV locais

## 🚀 Como Executar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama pull llama3.2:1b
ollama serve

# 3. Rodar
streamlit run src/app.py
```

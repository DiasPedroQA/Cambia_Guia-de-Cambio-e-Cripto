<!-- src/README.md -->

# 💱 Câmbia — Sua Guia de Câmbio e Cripto

> *"Porque dinheiro não precisa ser um bicho de sete cabeças — e câmbio muito menos."*

A **Câmbia** é um agente de IA generativa que te ajuda a acompanhar cotações de **dólar, euro e bitcoin**, gerenciar sua carteira de moedas e aprender sobre câmbio de um jeito leve, educativo e sem jargões chatos.

---

## 🧠 O que a Câmbia faz?

- ✅ Mostra cotações em **tempo real** (USD, EUR, BTC)
- ✅ Exibe sua **carteira pessoal** com valores sempre atualizados
- ✅ **Alerta você** quando o mercado oscila mais de 2%
- ✅ Ensina conceitos de câmbio e cripto **sem complicação**
- ✅ Sugere perguntas prontas pra você **explorar sem medo**
- ✅ Funciona **100% local** com Ollama — seus dados não saem da sua máquina

---

## 🧰 Stack do Projeto

|  Camada   |                                               Tecnologia                                                |
|-----------|---------------------------------------------------------------------------------------------------------|
| Interface |                                  [Streamlit](https://streamlit.io/) 🎈                                  |
| LLM Local |                            [Ollama](https://ollama.com/) + `llama3.2:1b` 🦙                             |
| Cotações  | [AwesomeAPI](https://docs.awesomeapi.com.br/) (USD/EUR) · [CoinGecko](https://www.coingecko.com/) (BTC) |
|  Dados    |                             JSON e CSV mockados (sem informações sensíveis)                             |
|  Visual   |                                 CSS customizado + badges interativos ✨                                 |

---

## 📁 Arquitetura de Pastas

```text
src/
├── app.py              # Ponto de entrada da aplicação
├── config.py           # Constantes e configurações gerais
├── tipos.py            # Tipos personalizados (TypedDict)
├── dados.py            # Carregamento dos arquivos JSON/CSV
├── cotacoes.py         # Conexão com APIs externas de cotação
├── prompts.py          # System prompt + montagem de contexto
├── ollama_cliente.py   # Comunicação com o modelo via Ollama
├── alertas.py          # Lógica de alertas proativos (som incluso!)
└── ui/
    ├── sidebar.py      # Sidebar com perfil e cotações
    ├── chat.py         # Chat interativo com quick replies
    ├── badges.py       # Badges de status do mercado
    ├── graficos.py     # Gráficos de evolução das cotações
    └── estilos.py      # Tema visual da Câmbia (CSS)
```

---

## 🚀 Como Rodar (do zero)

### 1. Instale o Ollama

```bash
# Baixe em ollama.com e depois:
ollama pull llama3.2:1b
```

### 2. Prepare o ambiente Python

```bash
# Crie o ambiente virtual
python3 -m venv .venv

# Ative (Linux/Mac)
source .venv/bin/activate

# Ative (Windows)
.venv\Scripts\activate

# Instale as dependências
pip install streamlit pandas requests
```

### 3. Inicie o Ollama (em outro terminal)

```bash
ollama serve
```

### 4. Rode a Câmbia 🎉

```bash
streamlit run src/app.py
```

Pronto! Acesse `http://localhost:8501` e converse com sua guia financeira pessoal.

---

## 📸 Evidência de Execução

> *Print da Câmbia funcionando lindamente:*

![Câmbia em execução](../assets/P5.png)

---

## 💡 Diferenciais deste Projeto

|         Diferencial         |                             Por que importa?                              |
|-----------------------------|---------------------------------------------------------------------------|
| 🎨 **Tema visual próprio**  |        CSS customizado, animações sutis e paleta de cores pensada         |
|   🔊 **Alertas sonoros**    |      Você escuta quando o mercado oscila — sem precisar olhar a tela      |
|    🧩 **Quick Replies**     |       Sugestões de perguntas prontas pra você explorar sem digitar        |
|  📊 **Badges de mercado**   |   Status visual rápido: "Dólar Baixo", "BTC Aquecido", "Mercado Aberto"   |
| 📈 **Gráficos de evolução** |              Mini-histórico de 24h pra cada moeda (simulado)              |
|   🧪 **Tipagem rigorosa**   |    TypedDict + Type Hints em todo o projeto — zero warnings do Pylance    |
|    🏗️ **Código modular**    | Cada responsabilidade em seu próprio arquivo — fácil de manter e expandir |

---

## 👩‍💻 Autoria

Feito com 💜, guaraná e curiosidade por Pedro Dias.

> *"Se você chegou até aqui, já sabe mais de câmbio do que 90% das pessoas. Bora aprender mais?"*

# 💱 Câmbia — Sua Guia de Câmbio e Cripto

> *"Porque dinheiro não precisa ser um bicho de sete cabeças — e câmbio muito menos."*

Agente de IA Generativa que monitora **dólar, euro e bitcoin** em tempo real, mostra sua carteira, alerta sobre oscilações e explica conceitos de câmbio de forma simples — **100% local, sem enviar seus dados pra lugar nenhum.**

---

## 🧠 O que a Câmbia faz?

- ✅ **Cotações em tempo real** — USD, EUR e BTC atualizados via API
- ✅ **Carteira consolidada** — patrimônio sempre visível na sidebar
- ✅ **Alertas automáticos** — avisa quando o mercado oscila mais de 2%
- ✅ **Quick Replies** — sugestões de perguntas prontas pra explorar
- ✅ **Badges de mercado** — status visual: "Dólar Baixo", "BTC Aquecido"
- ✅ **100% local** — Ollama + llama3.2:1b rodando na sua máquina

---

## 📸 Demonstração

|                       Tela principal                       |                   Chat em ação                    |
|:----------------------------------------------------------:|:-------------------------------------------------:|
| ![Tela principal](./assets/cambia-menu-lateral-aberto.png) | ![Chat](./assets/cambia-menu-lateral-fechado.png) |

|  Consulta de carteira  | Análise sobre bitcoin  |
|:----------------------:|:----------------------:|
| ![P1](./assets/P1.png) | ![P4](./assets/P4.png) |

---

## 🎬 Vídeo Pitch

[![Vídeo Pitch](https://img.youtube.com/vi/le9QLG0Wfvo/0.jpg)](https://www.youtube.com/watch?v=le9QLG0Wfvo)

> 📺 [Assistir ao Pitch da Câmbia no YouTube](https://www.youtube.com/watch?v=le9QLG0Wfvo) — *vídeo não listado*

---

## 🧰 Stack Tecnológica

|      Camada      |                  Tecnologia                   |
|------------------|-----------------------------------------------|
|    Interface     |      [Streamlit](https://streamlit.io/)       |
|       LLM        | [Ollama](https://ollama.com/) + `llama3.2:1b` |
| Cotações USD/EUR | [AwesomeAPI](https://docs.awesomeapi.com.br/) |
|    Cotação BTC   |    [CoinGecko](https://www.coingecko.com/)    |
|      Dados       |              JSON e CSV mockados              |
|      Visual      |     CSS customizado + badges interativos      |

---

## 📁 Estrutura do Projeto

```text
Cambia_Guia-de-Cambio-e-Cripto/
├── assets/              # Prints, vídeo pitch e materiais visuais
├── data/                # JSON e CSV com dados da cliente fictícia
├── docs/                # Documentação completa (6 etapas do desafio)
├── src/                 # Código-fonte modular
│   └── ui/              # Componentes de interface (sidebar, chat, badges)
├── app.py               # Ponto de entrada da aplicação
├── Makefile             # Automação de instalação e execução
├── requirements.txt     # Dependências do projeto
├── README.md            # Você está aqui
└── LICENSE              # Apache 2.0
```

---

## 🚀 Como Rodar

### Com Makefile (recomendado)

```bash
# 1. Instalar dependências e baixar modelo
make install
make ollama-pull

# 2. Em outro terminal, iniciar o Ollama
make ollama

# 3. Rodar a Câmbia
make run
```

### Manualmente

```bash
# 1. Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Baixar modelo e iniciar Ollama (em outro terminal)
ollama pull llama3.2:1b
ollama serve

# 4. Rodar a aplicação
streamlit run app.py
```

Acesse `http://localhost:8501` e comece a conversar com a Câmbia!

---

## ✨ Diferenciais

|        Diferencial         |                         Por que importa                          |
|----------------------------|------------------------------------------------------------------|
| 🎨 **Tema visual próprio** |        CSS customizado com animações, paleta roxa e verde        |
|   🔊 **Alertas sonoros**   |      Você escuta quando o mercado oscila — sem olhar a tela      |
|    🧩 **Quick Replies**    | Sugestões de perguntas prontas pra quem não sabe o que perguntar |
|  📊 **Badges de mercado**  |      Status visual rápido: "Dólar Baixo", "Mercado Aberto"       |
|  🧪 **Tipagem rigorosa**   |     TypedDict + Type Hints em todo o projeto — zero warnings     |
|   🏗️ **Código modular**    |        12 arquivos organizados por responsabilidade única        |

---

## 📊 Status do Projeto

|       Entregável        | Situação |
|-------------------------|----------|
| Documentação do agente  |    ✅    |
|  Base de conhecimento   |    ✅    |
|         Prompts         |    ✅    |
|   Aplicação funcional   |    ✅    |
|  Avaliação e métricas   |    ✅    |
|       Vídeo Pitch       |    ✅    |

---

## 👨‍💻 Autor

### **Pedro PM Dias**

Feito com 💜, café e curiosidade.

> *"Se você chegou até aqui, já sabe mais de câmbio do que 90% das pessoas."*

---

## 📜 Licença

Este projeto está sob a licença Apache 2.0. Consulte o arquivo [LICENSE](./LICENSE) para mais informações.

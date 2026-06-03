<!-- assets/README.md -->

# 🎨 Assets da Câmbia

> Prints, diagramas e materiais visuais do projeto.

---

## 📂 O que tem aqui?

|                 Arquivo                  |            O que mostra            |        Uso        |
|------------------------------------------|------------------------------------|-------------------|
|     `cambia-menu-lateral-aberto.png`     |   Interface completa com sidebar   |   Documentação    |
|    `cambia-menu-lateral-fechado.png`     |         Chat em foco total         |   Documentação    |
| `leu-a-pergunta-e-pensa-na-resposta.png` |         Agente processando         |   Documentação    |
|           `P1.png` a `P5.png`            | Exemplos de perguntas e respostas  | Galeria do README |
|         `video-pitch-cambia.mp4`         |         Pitch de 3 minutos         | Avaliação         |
|      `Câmbia - Guia de Câmbio.pdf`       |         Resumo do projeto          | Portfólio         |

---

## 📸 Galeria rápida

### Tela principal

![Menu Lateral Aberto](./cambia-menu-lateral-aberto.png)

### Chat em foco

![Menu Lateral Fechado](./cambia-menu-lateral-fechado.png)

### Exemplos de interação

|                Pergunta                 |    Resposta     |
|-----------------------------------------|-----------------|
| "Qual o valor total da minha carteira?" | ![P1](./P1.png) |
|       "Como está meu patrimônio?"       | ![P2](./P2.png) |
|        "Como está o dólar hoje?"        | ![P3](./P3.png) |
|     "Vale a pena comprar bitcoin?"      | ![P4](./P4.png) |
|         Continuação da análise          | ![P5](./P5.png) |

---

## 🎬 Vídeo Pitch

[🎥 Assistir no YouTube](https://www.youtube.com/watch?v=le9QLG0Wfvo) *(não listado)*

---

## 🏗️ Arquitetura

```mermaid
flowchart TD
    A[👤 Usuário] --> B[🎈 Streamlit]
    B --> C[🦙 Ollama]
    C --> D[📚 Dados locais]
    B --> E[💵 AwesomeAPI]
    B --> F[₿ CoinGecko]
    C --> G[💬 Resposta]
Stack: Streamlit · Ollama · llama3.2:1b · AwesomeAPI · CoinGecko · Python
```

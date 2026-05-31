<!-- docs/04-metricas.md -->

# Avaliação e Métricas da Câmbia

> Como saber se a Câmbia está realmente ajudando — ou só fazendo graça com cifrão?

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas e verifica se o agente entrega o combinado;
2. **Feedback real:** Pessoas reais testam o agente e dão notas com base na experiência de uso.

> 💡 Peça para 3-5 pessoas (amigos, família, colegas) testarem a Câmbia e avaliarem cada métrica
> com notas de 1 a 5. Isso torna suas métricas muito mais confiáveis!
> Lembre de contextualizar os participantes sobre a **cliente fictícia** Maria Oliveira.

---

## Métricas de Qualidade

|      Métrica      |             O que avalia             |                      Exemplo de teste                      |
|-------------------|--------------------------------------|------------------------------------------------------------|
| **Assertividade** |     A cotação informada é real?      |     Perguntar "qual o dólar hoje?" e conferir com API      |
|   **Segurança**   |          Inventou cotação?           |  Perguntar sobre moeda inexistente ("rublo bielorrusso?")  |
|   **Coerência**   | Resposta condiz com perfil moderado? |               Não sugerir alavancagem em BTC               |

---

## Cenários de Teste

### Teste 1: Consulta de cotação real

- **Pergunta:** "Qual o valor do euro?"
- **Resposta esperada:** Valor atualizado da AwesomeAPI com a fonte citada
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Alerta de variação

- **Pergunta:** (deixar o app aberto por alguns minutos)
- **Resposta esperada:** Se houve variação >2% no dólar ou bitcoin, a Câmbia mostra um alerta proativo
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo

- **Pergunta:** "Me indica um filme na Netflix?"
- **Resposta esperada:** Câmbia recusa educadamente e lembra que só fala de câmbio e cripto
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Dado inexistente

- **Pergunta:** "Qual a cotação do iene japonês?"
- **Resposta esperada:** Admite que não monitora o iene e oferece falar sobre dólar, euro ou bitcoin
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Formulário de Feedback

Use com os participantes do teste:

|    Métrica    |                            Pergunta                           | Nota (1-5) |
|---------------|---------------------------------------------------------------|------------|
| Assertividade | "As cotações e dados que a Câmbia mostrou estavam corretos?"  |    ____    |
|   Segurança   | "Ela inventou alguma informação ou admitiu quando não sabia?" |    ____    |
|   Coerência   |         "A linguagem foi clara, amigável e adequada?"         |    ____    |

**Comentário aberto:**
O que você achou da experiência? O que a Câmbia poderia fazer melhor?

---

## Resultados

Após os testes, registre suas conclusões:

### O que funcionou bem

- [ ] As cotações vieram sempre da API real, sem invenção
- [ ] A Câmbia recusou educadamente perguntas fora do escopo
- [ ] Os alertas de variação apareceram quando o mercado oscilou
- [ ] O tom informal e bem-humorado agradou os testadores
- [ ] As sugestões de perguntas prontas ajudaram quem não sabia o que perguntar

### O que pode melhorar

- [ ] Adicionar mais moedas monitoradas (libra, iene, Ethereum)
- [ ] Incluir gráfico de variação no próprio chat, não só na sidebar
- [ ] Permitir que o usuário atualize os saldos da carteira via chat
- [ ] Reduzir o tempo de resposta do llama3.2:1b em máquinas mais lentas
- [ ] Traduzir os termos técnicos automaticamente quando o usuário parecer iniciante

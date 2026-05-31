<!-- docs/02-base-conhecimento.md -->

# Base de Conhecimento da Câmbia

## Dados Utilizados

|          Arquivo          | Formato |                Função                 |
|---------------------------|---------|---------------------------------------|
|  `perfil_cambista.json`   |   JSON  |   Perfil da cliente Maria Oliveira    |
|  `carteira_moedas.csv`    |    CSV  | Histórico de compras/vendas de moedas |
| `historico_conversas.csv` |    CSV  |   Conversas anteriores com a Câmbia   |
| `moedas_disponiveis.json` |   JSON  |      Moedas que a Câmbia conhece      |

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados originais do desafio eram voltados para educação financeira tradicional (renda fixa, gastos mensais).
Para a Câmbia, todos os arquivos foram **recriados do zero** com o tema de câmbio e criptomoedas:

- **`perfil_cambista.json`**: Criado com campos como `saldo_usd`, `saldo_eur`, `saldo_btc` e uma meta de acumulação em dólar, refletindo o objetivo de diversificação cambial da Maria.
- **`carteira_moedas.csv`**: Substitui o `transacoes.csv` original — agora registra operações de compra/venda de moedas com cotação no momento da transação.
- **`historico_conversas.csv`**: Adaptado para temas de câmbio (dólar, euro, bitcoin) em vez de CDB, Tesouro Selic etc.
- **`moedas_disponiveis.json`**: Substitui `produtos_financeiros.json` — lista dólar, euro e bitcoin com volatilidade e indicações de uso.

Além disso, os dados são **enriquecidos em tempo real** com cotações da AwesomeAPI (USD/EUR) e CoinGecko (BTC),
algo que o template original não previa.

## Estratégia de Integração

Os dados são carregados no início da aplicação via `json.load` e `pd.read_csv`.
As cotações em tempo real vêm de APIs externas e atualizam o contexto antes de cada pergunta.

## Exemplo de Contexto Montado

```text
CLIENTE: Maria Oliveira, 28 anos
CARTEIRA ATUAL:
- USD: $1.500,00 (cotação: R$ 5,07)
- EUR: €800,00 (cotação: R$ 5,48)
- BTC: 0,015 (cotação: R$ 182.350,00)

ÚLTIMAS OPERAÇÕES:
- 25/10 vendeu 0,002 BTC a R$185.000
- 22/10 comprou €200 a R$5,45
```

# App-Vendas-Python
# Sistema de Pedidos de Açaí

Aplicação de terminal em Python simples para registrar pedidos de açaí e cupuaçu, calcular o valor de cada pedido e exibir o total acumulado ao final.

## Funcionalidades

- Exibição do cardápio com os preços por sabor e tamanho
- Escolha do sabor e do tamanho pelo terminal
- Validação das entradas, com nova solicitação em caso de valor inválido
- Cálculo do preço de cada pedido
- Soma acumulada de todos os pedidos da sessão
- Exibição do valor total ao encerrar

## Cardápio

| Tamanho | Cupuaçu (CP) | Açaí (AC) |
|---------|--------------|-----------|
| P       | R$ 9,00      | R$ 11,00  |
| M       | R$ 14,00     | R$ 16,00  |
| G       | R$ 18,00     | R$ 20,00  |

## Requisitos

- Python 3.6 ou superior (necessário para o uso de f-strings)

Não há dependências externas.

## Como executar

1. Clone o repositório ou baixe o arquivo do código.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python main.py
```

Substitua `main.py` pelo nome do arquivo no seu projeto.

## Como usar

1. Informe o sabor desejado: `CP` para cupuaçu ou `AC` para açaí.
2. Informe o tamanho desejado: `P`, `M` ou `G`.
3. O sistema exibe o preço do pedido.
4. Responda se deseja pedir mais alguma coisa: `S` para continuar ou `N` para finalizar.
5. Ao finalizar, o sistema exibe o valor total de todos os pedidos.

As entradas não diferenciam letras maiúsculas de minúsculas.

## Exemplo de execução

```
Bem-vindo(a) ao sistema de pedidos de Açaí! Meu nome é Gabriel Oliveira.

Digite o sabor desejado (CP/AC): ac
Digite o tamanho desejado (P/M/G): m

O preço do pedido é: R$16.00

Deseja pedir mais alguma coisa? (S/N): n

Obrigado por utilizar nosso sistema de pedidos! O valor total dos seus pedidos é: R$16.00
```

## Tratamento de entradas inválidas

- Sabor inválido: exibe a mensagem de erro e solicita o sabor novamente.
- Tamanho inválido: exibe a mensagem de erro e retorna ao início do pedido.
- Resposta diferente de `S` ou `N` na pergunta final: o programa informa a opção inválida e é encerrado.

## Conceitos aplicados

- Laço `while` com `break` e `continue`
- Estruturas condicionais `if`, `elif` e `else`
- Variável acumuladora
- Entrada de dados com `input()` e normalização com `.upper()`
- Formatação de valores monetários com f-strings

## Autor

Gabriel Oliveira

# Sistema Bancário - Trilha Python AI backend da DIO em parceria com a vivo
## Desafio do projeto
Este projeto tem como objetivo a criação da lógica de um sistema bancário na linguagem python.
Nesse primeiro momento o sistema contatará com 3 operações básica que poderão ser realizadas. Além das operações, teremos algumas regras de negócios que foram passadas no projeto.
# Requisitos do projeto
## depósito
O sistema conta com uma operação de depósito. O depósito só poderá ser realizado caso o valor informado para depósito seja um valor positivo. O valor informado para depósito será
salvo em uma variável chamada saldo que ficará disponível para outras operações no decorrer do ciclo de vida do programa. Nesse primeiro momento estamos trabalhando com apenas
uma conta, então não será necesário informar agência e conta.
## Saque
Podemos realizar operações de saque deduzindo o valor sacado da variável saldo. Para que o saque ocorra é necessário que o valor a ser sacado não exceda o saldo disponível para saque.
O sistema possui um limite de saque de 500 reais por transação e 3 saques por dia. Caso alguma dessas condições sejam excedidas o sistema apresentará erro e não permitirá o saque.
## Extrato
Todas as operações realizadas no programa são salvas em uma variável chamada extrato. Ela possui uma formatação de float para a precisão de duas casas decimais. O extrato exibirá todas
as operações realizadas e também o saldo final.

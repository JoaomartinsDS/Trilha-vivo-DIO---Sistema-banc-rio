# Sistema Bancário - Trilha Python AI backend da DIO em parceria com a vivo
## Desafio do projeto
Este projeto tem como objetivo a criação da lógica de um sistema bancário na linguagem python.
O projeto conta com algumas funções básicas que percebemos em sistemas bancários como depósito, saque e extrato. Além de função de criar usuário, criar conta e listar contas.
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
## Criar usuário
Podemos informar o CPF como input ao selecionar a opção de criar usuários. Temos uma estrutura condicional que irá tomar uma decisão a partir do filtro que procurar na lista que armazena os dados 
em tempo de execução, se o CPF já estiver cadastrado irá informar o cadastro e não permitir o input de novos dados. Caso o CPF não seja cadastrado, o sistema pedirá alguns dados para registrar o usuário em sistema
## Criar conta
A opção irá solicitar o CPF do usuário, caso seja um usuário cadastrado o sistema permitirá a criação de conta. Se não for umn usuário cadastrado irá apresentar uma mensagem informando que o usuário não está cadastrado. A criação de conta será através de uma agência padrão de número "0001". A conta será com base na quantidade de registros na variavel contas através da lógica len(contas)+1, que irá criar uma nova conta de maneira sucessiva sem repetir os dados da conta
## Listar conta
A partir da variavel conta que é um lista, criamos uma estrutura de repetição em que acessára o nome do titular dentro de um dicionário na variavel contas, e irá apresentar os dados da conta, no seguinte formato:
Titular: XXXXXX
Agência: XXXXX
Conta: XXXXXX

#FIXME -  funções
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

print('Cadastro realizado')
def criar_conta():
    global saldo
    saldo = 0.0
    print('Conta criada...')

def mostrar_dados():
    print(f'Nome: {nome}')
    print(f'Saldo: R${saldo:.2f}')

def depositar():
    global saldo
    valor = float(input('Digite um valor para depositar: R$ '))
    if valor > 0:
        saldo += valor
        print(f'Depósito realizado! Novo saldo: R$ {saldo:.2f}')
    else:
        print('Valor inválido!')
def sacar():
    global saldo
    valor = float(input('Digite o valor para sacar: R$ '))
    if 0 < valor <= saldo:
        saldo -= valor
        print(f'Saque realizado! Novo saldo: R$ {saldo:.2f}')
    else:
        print('Saldo insuficiente ou valor inválido!')
def sair():
    print('Saindo...')
    exit()

while True:
    print('--- MENU BANCO ---')
    print('1 - Criar conta bancaria')
    print('2 - Mostrar dados da conta')
    print('3 - Depositar')
    print('4 - Sacar')
    print('5 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        mostrar_dados()
    elif opcao == '3':
        depositar()
    elif opcao == '4':
        sacar()
    elif opcao == '5':
        sair()
    else:
        print('Opção inválida!')
saldo = 0.0
nome = None

def criar_conta():
    """Cria uma nova conta bancária com saldo inicial zero."""
    global nome, saldo
    nome = input("Digite o nome do usuário: ")
    saldo = 0.0
    print(f"\n Conta criada para {nome} com saldo inicial de R${saldo:.2f}")

def exibir_dados():
    """Mostra os dados da conta (nome e saldo)."""
    if nome:
        print(f"\n Titular: {nome}")
        print(f" Saldo atual: R${saldo:.2f}")
    else:
        print("\n Nenhuma conta foi criada ainda.")

def depositar(valor):
    """Adiciona um valor positivo ao saldo da conta."""
    global saldo
    if valor > 0:
        saldo += valor
        print(f"\n Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("\n Valor de depósito inválido.")

def sacar(valor):
    """Remove um valor do saldo, se houver fundos suficientes."""
    global saldo
    if valor <= 0:
        print("\n O valor de saque deve ser maior que zero.")
    elif valor > saldo:
        print("\n Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor
        print(f"\n Saque de R${valor:.2f} realizado com sucesso!")

def encerrar_conta():
    """Encerra a conta apenas se o saldo for zero."""
    global saldo, nome
    if not nome:
        print("\n Nenhuma conta foi criada ainda.")
    elif saldo != 0:
        print("\n Não é possível encerrar a conta com saldo diferente de zero.")
    else:
        print(f"\n Conta de {nome} encerrada com sucesso.")
        nome = None

def sair():
    """Sai do sistema."""
    print("\n Saindo do sistema. Obrigado por utilizar nossos serviços!")
    exit()

# Programa principal
print(" Bem-vindo ao sistema bancário!")
while True:
    print("\n===== MENU =====")
    print("1 - Criar Conta")
    print("2 - Exibir Dados")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Encerrar Conta")
    print("6 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        exibir_dados()
    elif opcao == '3':
        if nome:
            valor = float(input("Digite o valor para depósito: R$"))
            depositar(valor)
        else:
            print("\n Crie uma conta antes de depositar.")
    elif opcao == '4':
        if nome:
            valor = float(input("Digite o valor para saque: R$"))
            sacar(valor)
        else:
            print("\n Crie uma conta antes de sacar.")
    elif opcao == '5':
        encerrar_conta()
    elif opcao == '6':
        sair()
    else:
        print("\n Opção inválida. Tente novamente.")

# lista de nomes

nomes = []

while True:
    print('1 - Inluir nome')
    print('2 - Pesquisar nome')
    print('3 - Alterar nome')
    print('4 - Excluir nome')
    print('5 - Mostrar nome')
    print('6 - Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        nome = input('Digite o nome para incluir: ')
        nomes.append(nome)
        print(f'{nome} foi adicionado à lista')
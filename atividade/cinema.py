print(40*'-',"FILMES", 40*'-')
idade = int(input('Digite a sua idade: '))
print()
while True:
    print("Sala 1 - Clube da Luta | Classificação indicativa: 18 anos")
    print("Sala 2 - Coringa | Classificação indicativa: 16 anos")
    print("Sala 3 - Pantera Negra| Classificação indicativa: 14 anos")
    print("Sala 4 - Harry Potter e o Prisioneiro de Azkaban | Classificação indicativa: 12 anos")
    print("Sala 5 - Toy Story 3| Classificação indicativa: 10 anos") 
    print('Digite ''sair'' para encerrar o programa.')
    opcao = input('Escolha a sala (exemplo: Sala 1) ou sair: ')
    print()
    if opcao == "sair":
        print('Programa encerrado. Até logo!')
        break
    if opcao == "Sala 1":
        if idade >= 18: 
            print('Ingresso comprado🎟️')
            break
        else:
            print('Idade inadequada')
    elif opcao == "Sala 2":
        if idade >= 16: 
            print('Ingresso comprado🎟️')
            break
        else:
            print('Idade inadequada')
    elif opcao == "Sala 3":
        if idade >= 14: 
            print('Ingresso comprado🎟️')
            break
        else:
            print('Idade inadequada')
    elif opcao == "Sala 4":
        if idade >= 12: 
            print('Ingresso comprado🎟️')
            break
        else:
            print('Idade inadequada')
    elif opcao == "Sala 5":
        if idade >= 10: 
            print('Ingresso comprado🎟️')
            break
        else:
            print('Idade inadequada')
    else: 
        print('Opção inválida, tente novamente.')
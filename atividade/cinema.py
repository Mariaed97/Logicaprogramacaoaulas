print(40*'-',"FILMES", 40*'-')
idade = int(input('Digite a sua idade: '))
print()

while True:
    print("Sala e Filme 1 | Classificação indicativa: 18 anos")
    print("Sala e Filme 2 | Classificação indicativa: 16 anos")
    print("Sala e Filme 3 | Classificação indicativa: 14 anos")
    print("Sala e Filme 4 | Classificação indicativa: 12 anos")
    print("Sala e Filme 5 | Classificação indicativa: 10 anos") 

    opcao = input('Escolha um filme: ')

    if opcao == "Filme 1":
        if idade >= 18: 
            print('Ingresso comprado')
            break
        else:
            print('Idade inadequada')
    if opcao == "Filme 2":
        if idade >= 16: 
            print('Ingresso comprado')
            break
        else:
            print('Idade inadequada')
    if opcao == "Filme 3":
        if idade >= 14: 
            print('Ingresso comprado')
            break
        else:
            print('Idade inadequada')
    if opcao == "Filme 4":
        if idade >= 12: 
            print('Ingresso comprado')
            break
        else:
            print('Idade inadequada')
    if opcao == "Filme 5":
        if idade >= 10: 
            print('Ingresso comprado')
            break
        else:
            print('Idade inadequada')
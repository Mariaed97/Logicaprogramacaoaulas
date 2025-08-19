'''
Programa: Sorteio V.2.0
Importando Bibliotecas 
Aula 04: 19/08

Raandom: escolha aleatoria
Descrição: sistema recebe o nome dos candidados e realiza o sorteio
'''

# importando bibliotecas

import random

lista = []

sair = False

while sair == False:
    nome_candidato = input('Digite os nomes para o sorteio ou enter para sair: ')
    if nome_candidato != "":
        # append - adiciona o valor da variavel dentro da lista
        lista.append(nome_candidato)
    else: 
        sair = True
escolhido =  random.choice(lista)

print('Escolhido foi:', escolhido)







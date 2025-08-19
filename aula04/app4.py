'''
Programa: Sorteio V.3.0
Importando Bibliotecas 
Aula 04: 19/08

Raandom: escolha aleatoria
Descrição: sistema recebe o nome dos candidados e realiza o sorteio
'''

# importando lib
import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input('Digite o nome para o sorteio: ')
    if nome:
        lista_nomes.append(nome)
    else:
        break

while True:
    if lista_nomes:
        os.system('cls')
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)
        # excluir o sorteado da lista original
        '''
        pop - função, remove pelo indice
            pop() - remover o ultimo indice
            pop(0) - remove o indice 0
        del - instrução, remove item pelo indice, mais de um item
            del[1:10]
        remove - remove a partir de uma variavel
            lista.remove(variavel)
        '''

        print(f'O escolhido foi: {escolhido}')
        lista_nomes.remove(escolhido)


        opcao = input('Deseja sortear outro nome? S - Sim \n| N - Não\n: ').lower()
        os.system('cls')

        if opcao != 's':
            break
    else: 
        print('Não há nomes para serem sorteados!')
        break
print('Programa finalizado!')
print(f'Os sorteados foram {lista_sorteados}')


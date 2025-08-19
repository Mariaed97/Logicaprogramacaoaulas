#FIXME - Coleções Parte 1: Lista
'''
# lista
nome_lista = ['Fulano', 'Ciclano', 'Beltrano', 'Joana']
# imprime lista na tela
print(nome_lista)

print()

# lista 
nome_lista = ['Fulano', 'Ciclano', 'Beltrano', 'Maria' ]
print(nome_lista[0]) # exibe o primeiro nome da lista
print(nome_lista[2]) # exibe o terceiro nome da lista

print()

# lista
nome_lista = ['Fulano', 'Ciclano', 'Beltrano', 'Joana']
# percorrendo a lista
for nome in nome_lista:
    print(nome)

print()

# lista
nome_lista = ['Maria', 'Pedro', 'João', 'Karla', 'Joana']
# percorrendo a lista com um contador
for i in range(len(nome_lista)):
    print(f'{i + 1}º nome da lista: {nome_lista[i]}')

print()

# Forma 1: operador in - encontrar algo dentro de uma lista

nomes_lista = ['Maria', 'Pedro', 'João', 'Karla', 'Joana']
nome = input('Informe o nome que dejeja encontrar algo: ')

if nome in nomes_lista:
    print(nome)
else:
    print(f'{nome} não encontrado. ')

print()

# Forma 2: index - buscar elementos na lista
nomes_lista = ['Maria', 'Pedro', 'João', 'Karla', 'Joana']
nome = input('Informe o nome que dejeja encontrar algo: ')
# procura pelo indice atraves do valor
indice = nomes_lista.index(nome)
# retorna o resultado
try:
    print(f'{nome} encontrado no índice {indice}.')
except: 
    print(f'{nome} não encontrado')

print()

# Forma 3: Count - para contar a quantidade de um determinado elemento em uma lista:
nomes_lista = ['Maria', 'Pedro', 'João', 'Karla', 'Joana', 'Maria']
nome = input('Informe o nome que dejeja encontrar algo: ')

# conta a qntd de vezes q o valor foi encontrado
quantidade = nomes_lista.count(nome)

# retorna resultado
try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes')
except:
    print(f'{nome} não foi encontrado')

# alterando dadod de uma lista
nomes_lista = ['Fulano', 'Ciclano', 'Beltrano', 'Maria', 'Joana', 'Fulano']
nomes_lista[0] = 'Alex'

for nome in nomes_lista:
    print(nome)

# mas se nao souber o indice, pode fazer uma pesquisa pelo nome e pedir para retornar seu indice
nomes_lista = ['Fulano', 'Ciclano', 'Beltrano', 'Maria', 'Joana', 'Fulano']
nome_a_alterar = input('Informe o nome que deje alterar: ')
nomes_lista[nomes_lista.index(nome_a_alterar)] = input('Informe o nome nome: ')

for nome in nomes_lista:
    print(nome)

# tabuada

numero = int(input('Digite o numero: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{i} X {numero} = {resultado}')
'''
#FIXME - !
"""
Programa: Contagem regressiva
Importando Bibliotecas
aula-19/08

# importando bibliotecas (lib)
import os
from time import sleep

cont = input('Digite um numero inteiro: ')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'Contagem regressiva: {cont_int}...')
        sleep(1)
        cont_int -= 1

except:
    print('Digite um numero válido!')

print('Fim da contagem')
"""

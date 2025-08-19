'''
Programa: Adivinhação V.1.0
Importando Bibliotecas 
Aula 04: 19/08

Raandom: escolha aleatoria
'''
# importando lib
from random import randint

print('Tente adivinhar o número!')
num1 = int(input('Digite um número: '))

num_secreto = randint(1,10)

if num1 == num_secreto:
    print('Parabens, voce ganhou!')
else:
    print('Voce perdeu')
    print(f'o numero correto era {num_secreto}')
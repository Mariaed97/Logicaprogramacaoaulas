'''
Programa: Adivinhação V.2.0
Importando Bibliotecas 
Aula 04: 19/08

Raandom: escolha aleatoria
'''
# importando lib
import random
import os 
import time
numero_secreto = random.randint(1,100)

tentativas = 0
max_tentativas = 10
acertou = False

print(30*'-', 'Bem vindo ao adivinha aí', 30*'-')
print(f'Você tem {max_tentativas} tentativas para adivinhar o número secreto')
print('Vamos começar?')

while tentativas < max_tentativas:
    try:
        # entrada do usuario
        palpite = int(input('Digite seu palpite: '))

    except ValueError:
        print('Por favor, digite um número valido.')
        continue

    tentativas += 1

    # verificar palpite
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um número maior!')
        time.sleep(3)
        os.system('cls')
    else: 
        print('Tente um número menor!')
        time.sleep(3)
        os.system('cls')

if acertou:
    print(f'Parabéns você ganhou! você acertou o número {numero_secreto} em {tentativas} tentativas')
else: 
    print(f'Que penaa! Você não conseguiu acertar, o número certo é {numero_secreto}')
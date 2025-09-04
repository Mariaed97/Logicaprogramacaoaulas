# gerador de senha aleatoria

import random
import string

def gerar_senha(comprimento=12, incluir_maiucuculo=True, incluir_minusculo=True,
                incluir_numeros=True, incluir_caracter=True):
    
    caracteres = ''
    if incluir_maiucuculo:
        caracteres += string.ascii_uppercase

    if incluir_minusculo:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracter:
            caracteres += string.punctuation
    
    if not caracteres:
         return ValueError('Deve ter pelo menos um tipo de caracter')
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'Senha: {senha}')
    return senha

def main():
    print('Gerador de senhas fortes')
    comprimento = int(input('Digite o comprimento da senha (padrão é 12): ') or 12)
    incluir_maiuscula = input('Incuir maiúscula (s/n, padrão = sim): ').lower() != 'n'
    incluir_minuscula = input('Incuir minuscula (s/n, padrão = sim): ').lower() != 'n'
    incluir_numeros = input('Incuir números (s/n, padrão = sim): ').lower() != 'n'
    incluir_caracter_esp = input('Incuir caracter especial (s/n, padrão = sim): ').lower() != 'n'

    senha = gerar_senha(comprimento, incluir_maiuscula, incluir_minuscula, incluir_numeros,
                        incluir_caracter_esp)
    
    print(f'A senha gerada foi: {senha}')

    with open('aula08/senhas.txt', 'a') as s:
        s.write(f'\n{senha}')


if __name__ == '__main__':
    main()
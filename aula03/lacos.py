
'''
Problema: crie um sistema que calcula o indice de massa corporal (IMC)
do usuario, mostre o valor do IMC na tela, e retorne se o usuario esta
no peso ideal ou se precisa emagrecer ou engordar mais> utilize a tabela
do IMC para definir os valores

imc = peso/(altura * altura)

18,5 ou menos 
Abaixo do normal

entre 18,5 e 24,9
Normal

entre  24,9 e 29,9
Sobrepeso

entre 29,9 e 34,9
obesidade grau I

entre 34,9 e 39,9
obesidade grau II

acima disso
obesidade grau III


print(40*'-',"CALCULADORA DE IMC", 40*'-')

while True:
    altura = float(input('Digite sua altura: ').replace(',','.'))
    peso = float(input('Digite seu peso: ').replace(',','.'))

    imc = peso/(altura * altura)
    print()
    print(f'Seu IMC é: {imc:.2f}')

    if imc <= 18.5:
        print('Abaixo do normal')
    elif imc <= 24.9:
        print('Normal')
    elif imc <= 29.9:
        print('Sobrepeso')
    elif imc <= 34.9:
        print('Obesidade grau I')
    elif imc <= 39.9:
        print('Obesidade grau II')
    else:
        print('Obesidade grau III')
    opcao = input('Deseja calcular novamente? S - Sim | N - Não').lower()

    if opcao == 's':
        continue
    elif opcao == 'n':
        print('Saindo do sistema!')
        break
    else: 
        print('Opção inválida')
'''


'''
Problema 2: Um elevador de carga possui capacidade para 200kg. Crie um programa
que receba do usuario seu peso e o peso da carga e verifica se a carga está autorizada 
a usar o elevador ou não.
'''

limite = 200
peso_pessoa = float(input('Digite seu peso: ').replace(',','.'))
peso_carga = float(input('Digite o peso da carga: ').replace(',','.'))

if (peso_pessoa + peso_carga) <= limite:
    print('Carga autorizada!')
else: 
    print('Carga não autorizada!')

#ANCHOR - LAÇOS

'''
#FIXME -  laço while - criado para criar loops infinitos, por isso precisa de uma condição para ser parado
# declaração de variavel
numero = 10 

# loop
while numero >= 0:
    print(numero)
    numero -= 1
'''
'''
#FIXME - Continue
cont = 0 

while cont < 10:    
    cont += 1
    if cont % 2 == 0:
        print(cont)
    else:
        continue
    print('Contando...')
'''

'''

#FIXME - Break - ele acaba com o loop e vai pro final do programa
cont = 0
while cont < 15: 
    cont += 1
    if cont % 2 == 0:
        print(cont)
    elif cont >=7:
        break
    else:
        continue
    print('contando')

# a calculadora foi colocada em loop 
'''

print(40*'-',"CADASTRO DE USUÁRIO", 40*'-')
nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
telefone = input('Digite seu Telefone: ')
dt_nascimento = int(input('Digite seu ano de nascimento: '))
print(80*'=')

while True:
    # menu principal
    print(40*'-',"Sistema Console 2° DS", 40*'-')
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Feliz Natal')
    print('6 - Sair')

    opcao = input('Digite uma opção: ')

    if opcao == "1":
        altura = float(input('Digite sua altura: ').replace(',','.'))
        peso = float(input('Digite seu peso: ').replace(',','.'))

        imc = peso/(altura * altura)
        print()
        print(f'Seu IMC é: {imc:.2f}')

        if imc <= 18.5:
            print('Abaixo do normal')
        elif imc <= 24.9:
            print('Normal')
        elif imc <= 29.9:
            print('Sobrepeso')
        elif imc <= 34.9:
            print('Obesidade grau I')
        elif imc <= 39.9:
            print('Obesidade grau II')
        else:
            print('Obesidade grau III')
    elif opcao == '2':
        ano_atual = 2025
        idade = ano_atual - dt_nascimento
        print(nome, 'é maior de idade.' if idade >=18 else 'é menor de idaade.')
    elif opcao == '3':
        print("Calculadora")
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        while True:
            print('1 - Soma')
            print('2 - Divisão')
            print('3 - Subtração')
            print('4 - Multiplicação')
            print('5 - Sair')

            opcao_calculo = input('Escolha uma operação matemática: ')

            if opcao_calculo == '1':
                print(f'Resultado da Soma é: {num1 + num2}')
            elif opcao_calculo == '2':
                print(f'Resultado da Divisão é: {num1/num2}')
            elif opcao_calculo == '3':
                print(f'Resultado da Subtração é: {num1 - num2}')
            elif opcao_calculo == '4':
                print(f'Resultado da Multiplicação é: {num1 * num2}')
            elif opcao_calculo == '5':
                break
            else: 
                print('Opção inválida')
    elif opcao == '4':
        print(f'Nome: {nome} | Telefone: {telefone} |')
        print (f'CPF: {cpf} | Data de Nascimento: {dt_nascimento} |')
        print(50*'-')
    elif opcao == '5':
        linhas =  6
        j = 1

        while j<= linhas:
            espacos = linhas - j
            estrelas = 2 * j - 1

            print(' ' * espacos + "❤️" * estrelas)
            j +=1
    elif opcao == '6':
        print('Saindo do sisema!')
        break
    else: 
        print('Opção inválida!')

'''
#FIXME - LAÇO FOR - declarado varias vezes dentro do cod., ele acaba nao é um loop infinito, é o programa q define onde para não o usuario
# exemplo
for n in range(5):
    print(n)
# no terminal ele fai do 0 ao 4 (depende do n° que esta dentro do ())

nome = 'Maria'

for i in nome:
    print(i)
''' 
print("olá, mundo")
print("olá, mundo")
print(50*"-","Concatenando texto", 40*"-")
print("esse é meu primeiro \nscript em python")
# comentario de linha 
'''
criar um sistema para mostrar meu nome, idade e data de nascimento
'''
nome = "Maria Eduarda"
idade = "17"
dt = "20/05" 
print("meu nome é:",nome)
print("tenho",idade,"anos")
print("minha data de nascimento:",dt)
# Tipos de variaveis
nome = "Maria"
idade = 17
altura = 1.62
ativo = True
print("O tipo da variavel nome é:",type(nome))
print("O tipo da variavel idade é:",type(idade))
print("O tipo da variavel altura é:",type(altura))
print("O tipo da variavel ativo é:",type(ativo))

# operadores
print(30*"-","operações",30*"-")
num1 = 8
num2 = 2
soma = num1 + num2
divisao = num1 / num2 # divisão comum
divi_inteira = num1 // num2 # divisao inteira
mult = num1 * num2
expo = num1 ** num2
subt = num1 - num2
resto = num1 %2
print('Resultado da soma',num1, "+", num2, "é:", soma)
print('Resultado da divisão',num1, "/", num2, "é:", divisao)
print('Resultado da divisão inteira',num1, "//", num2, "é:", divi_inteira)
print('Resultado da multiplicação',num1, "*", num2, "é:", mult)
print('Resultado do expoente',num1, "**", num2, "é:", expo)
print('Resultado da subtração',num1, "-", num2, "é:", subt)
print('Resultado do resto',num1, "é:", resto)

print()
print(30*'-','operadores de comparação',30*'-')
#operadores de comparação
num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print("ano atual:",ano)
ano += 1
print("ano acrecido de +1:",ano)
ano -= 1
print("ano decrecido de -1:",ano)

# operadores logicos
# AND, OR, NOT

print()
print(30*'-','Entrada de dados',30*'-')

nome_usuario = input("Digite o seu nome: ")
print('Seja bem-vindo ao sistema python', nome_usuario)

print()
print(30*'-','Calculadora',30*'-')

numero1 =int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# tipos de dados
# float = numeros reais, ou seja, tem ',', exemplo: 5.20
# int = numeros inteiros
# str = texto, conjunto de caracteres
# bool = valores logicos como True e False

soma = numero1 + numero2
divisao = numero1 / numero2
mult = numero1 * numero2
sub = numero1 - numero2

print('Resultado da soma',numero1, "+", numero2, "é:", soma) 
print('Resultado da divisão',numero1, "/", numero2, "é:", divisao)
print('Resultado da multiplicação',numero1, "*", numero2, "é:", mult)
print('Resultado da subtração',numero1, "-", numero2, "é:", sub)

print()
print(30*'-','Convertendo tipos de dados',30*'-')

ano_nascimento = input('Digite seu ano de nascimento: ')
print(type(ano_nascimento))

# convertendo para inteiro 

ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))

n1 = 10
n2 = 20
print("a soma é:", n1+n2, type(n1), float(n2))

saudacao = input('Digite seu nome: ')
cpf = input('digite seu cpf: ')
telefone = input('digite seu telefone: ')

print()
print(30*'-','dados pessoais',30*'-')
print('Nome:', saudacao)
print('CPF:', cpf, '| Telefone:', telefone)
print(50*'-')
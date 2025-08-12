# concatenação
# quebra de linha
# formatando decimais
# alterando  vírgula e ponto 
# if else
# operador ternario

'''
comandos: 
cd = abrir uma pasta
cd.. = voltar na pasta anterior
ls = listar 
dim = listar diretorio
cls = limpa o terminal
'''
nome = "Maria"
idade = 17
altura = 1.61

#FIXME - concatenação com ,
print('Olá, meu nome é,', nome,',tenho', idade, ' anos de idade') 
#FIXME - concatenação com format 
print('Olá, meu nome é, {} , tenho {} anos de idade' .format(nome,idade)) 
#FIXME - concatenação com f-string
print(f'olá, meu nome é {nome} e tenho {idade} anos de idade')
#FIXME - concatenação com +
print('olá, meu nome é, ' + nome + ', tenho ' + str(idade)+ 'anos de idade')

# eliminando quebra de linha
print('O sábio sabia ', end='')
print('que sabiá sabia assoviar.') 


valor = 1.23456789

# exibindo o valor com duas casas depois da virgula
print(f'{valor:,.2f}')
print(f'{valor:.3f}')

print(50*'=')
peso = input('digite seu peso: ').replace(',','.')
peso = float(peso)
# replace vai servir para mudar a virgula que o usuario colocar por ponto
print(f'{peso:.2f}')


print()
print(30*'-','Atividade',30*'-')
# atividade 3 = criar um programa que peça o nome do usuário e exiba uma mensagem de boas-vindas
nome = input('Digite seu nome: ')
print(f'Olá, seja bem-vindo(a), {nome}, ao sistema.')

#FIXME - if e else
# variaveis
nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))
# estrutura de decisão
if idade >= 18:
    print('Você é maior de idade!')
    print('Você está dentro do bloco IF')
else:
    print('Você é menor de idade!')
    print('você está dentro do bloco Else')
print('você está fora da estrutura condicional')


num1 = 10

if num1 %2 ==0:
    print('numero par')
else:
    print('numero impar')

print(40*'-','BOLETIM ESCOLAR',40*'-')
# upper - caixa alta; lower - caixa baixa
nome_aluno = input('Digite o nome do aluno: ').upper()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

# >= 7: aprovado
# >= 5: recuperação
# reprovado

if media >=7:
    print(f'{nome_aluno}!!!Aluno Aprovado')
    print(f'Nota1: {nota1} | Nota 2:  {nota2}')
    print(f'Nota3: {nota3} | Nota 2:  {nota4}')
    print(20*"=")
    print(f'Média: {media}')

elif media >=5:
    print(f'{nome_aluno}!!!Aluno de recuperação')
    print(f'Nota1: {nota1} | Nota 2:  {nota2}')
    print(f'Nota3: {nota3} | Nota 2:  {nota4}')
    print(20*"=")
    print(f'Média: {media}')

else: 
    print(f'{nome_aluno}!!!Aluno Reprovado')
    print(f'Nota1: {nota1} | Nota 2:  {nota2}')
    print(f'Nota3: {nota3} | Nota 2:  {nota4}')
    print(20*"=")
    print(f'Média: {media}')
  

# variaveis
nome =  input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

# verifica se o usuario possui os requisitos minimos
if idade >= 12 and altura >= 1.2:
    print(f'A entrada de {nome} está autorizada')
else:
    print(f'A entrada de {nome} não está autorizada')


#FIXME - - operador ternario

# variaveis
nome = "Marcos"
idade = 45
# operador ternario
print(nome, 'é maior de idade.' if idade >= 18 else ' é menor de idade.')

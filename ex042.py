#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
#será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

r1 = int(input('Digite o primeiro comprimento: '))
r2 = int(input('Digite o segundo comprimento: '))
r3 = int(input('Digite o terceiro comprimento: '))
#primeira validação 'se é triângulo':
if r1 < r2 + r3 and r1 < r3 + r2 and r3 < r1 + r2:
    print('Sim, é possível formar um triângulo com os valores fornecidos.')
    #se é Equilatero
    if r1 == r2 == r3:
        print('Seu triângulo é EQUILÁTERO')
    #se é Isosceles
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Seu triângulo é ISÓSCELES')
    #se é Escaleno
    else:
        print('Seu triângulo é ESCALENO')
else: 
    print('Não é possível formar um triângulo com os valores fornecidos.')
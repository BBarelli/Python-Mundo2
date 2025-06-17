#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo

r1 = int(input('Digite o primeiro comprimento: '))
r2 = int(input('Digite o segundo comprimento: '))
r3 = int(input('Digite o terceiro comprimento: '))
#condição:
if r1 < r2 + r3 and r1 < r3 + r2 and r3 < r1 + r2:
    print('Sim, é possível formar um triângulo com os valores fornecidos.')
else: 
    print('Não é possível formar um triângulo com os valores fornecidos.')

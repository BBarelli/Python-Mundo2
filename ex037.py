# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))
# print com aspas triplas permite a digitação de várias linhas
print('''Escolha uma das bases:      
[1. Binário]
[2. Octal]
[3. Hexadecimal]''')

escolha = int(input('Escolha uma opção: '))

if escolha == 1:
    print(f'O numero {numero}, convertido pra Binário é: {bin(numero)[2:]}')# [2:] tecnica de fatiamento

elif escolha == 2:
    print(f'O numero {numero}, convertido pra Octal é: {oct(numero)[2:]}')# [2:] tecnica de fatiamento

elif escolha == 3:
    print(f'O número {numero}, convertido pra Hexadecimal é: {hex(numero)[2:]}')# [2:] tecnica de fatiamento

else:
    print('Opção inválida, tente novamente.')


# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'O número foi divisivel por {num} e {tot} vezes.')
if total == 2:
    print('Seu número é primo')
else:
    print('Seu número não é primo')
   


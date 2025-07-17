#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

t = int(input('Digite um número como termo: '))
r = int(input('Digite um número como razão: '))
termo = t
cont = 1
while cont <= 10:
    print(f'{termo} ', end='')
    termo += r
    cont += 1
print('Fim')
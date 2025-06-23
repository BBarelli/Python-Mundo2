# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma P.A
# No final, mostre os 10 primeiro termos dessa progressão
i = int(input('Digite o primeiro termo: '))
r = int(input( 'Digite a razão: '))
for c in range(0, 10):
    termo = i + c * r
    print(termo)
print('FIM')

# Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
# e que se encontram no intervalo de 1 até 500
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c # s += c
print(f'O somatorio entre os valores impares é de: {s}')
print('Fim')
        
    
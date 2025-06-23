# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar desconsidere
s = 0
for c in range(1, 7):
    n = int(input('Digite seu número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos valores pares é de: {s}')
print('Fim')
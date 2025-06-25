# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
# Maior / Menor em uma lista
maior_peso = 0
menor_peso = 0
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}º pessoa: '))
    if pessoa == 1:  # estabelecendo onde será guardado o primeiro peso que for digitado
        maior_peso = peso  # iniciando a partir da primeira digitação, até o momento esse é o maior
        menor_peso = peso  # iniciando a partir da primeira digitação, até o momento esse é o menor
    else:
        if peso > maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso contabilizado foi de {maior_peso}kg')
print(f'O menor peso contabilizado foi de {menor_peso}kg')

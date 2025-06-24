# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.

from datetime import date

data_atual = date.today().year 
total_maior = 0 #Variavél 
total_menor = 0
for pessoa in range (1, 8):
    ano = int(input(f'Digite o ano de nascimento da {pessoa}: '))
    idade = data_atual - ano

    if idade >= 21:
        total_maior += 1 # variavel criada pra contabilizar
    else:
        total_menor += 1 # variavel criada pra contabilizar

print(f'Foi contabilizado {total_maior} pessoas maior de idade e {total_menor} pessoas menor de idade.')

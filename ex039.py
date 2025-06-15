#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe:
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
#print(idade)
if idade >= 18:
    print('Você foi convocado! Apresente a base militar mais próxima da sua casa.')
    print('Essa é a hora exata para servir ao seu país.')
elif idade < 18:
    print('Entendemos sua vontande de servi ao Exécito Brasileiro, mais ainda não pussi a idade minima.')
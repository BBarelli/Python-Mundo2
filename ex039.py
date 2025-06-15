#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe:
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
ano_atual = date.today().year
#print(idade)
if idade == 18:
    print('Você foi convocado! Apresente a base militar mais próxima da sua casa.')
    print('Essa é a hora exata para servir ao seu país.')

elif idade < 18:
    anos_faltam = 18 - idade
    ano_alistamento = anos_atual + anos_faltam
    print(f'Ainda não é possível, faltam {anos_faltam} anos, seu ano de alistamento será em {ano_alistamento}')

else:
    anos_passado = idade - 18
    print(f'Entendemos sua vontande de servi ao Exécito Brasileiro, mas já passou {anos_passado} Anos do limite.')

 

'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia:
#o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER'''

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('De acordo com sua idade sua categoria é: MIRIM')
    print('Alunos até 9anos')
elif idade <= 14:
    print('De acordo com sua idade sua categoria é: INFANTIL')
    print('Alunos com idade entre 10 a 14 anos.')
elif idade <= 19:
    print('De acordo com sua idade sua categoria é: JÚNIOR')
    print('Alunos com idade entre 15 a 19 anos.')
elif idade <= 25:
    print('De acordo com sua idade sua categoria é: SÊNIOR')
    print( 'Alunos com idade entre 20 a 25 anos.')
else:
    print('De acordo com sua idade sua categoria é: MASTER')
    print('Alunos acima de 25 Anos.')

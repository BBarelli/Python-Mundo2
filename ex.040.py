#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2) / 2

if media > 7:
    print(f'Parabéns você foi APROVADO! com média {media}')
elif media > 5 and media <= 6.9:
    print('Infelizmente você ficou de RECUPERAÇÃO, acreditamos em você')
else:
    print('Seu resultado não foi satisfatório você está REPROVADO') 
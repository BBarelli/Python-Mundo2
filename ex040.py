#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'Parabéns você foi APROVADO com média {media}.')
elif 5 <= media > 7:
    print(f'Sua media foi: {media}, você esta de recuperação.') 
else:
    print('Infelizmente sua média foi abaixo do esperado, você foi REPROVADO.')
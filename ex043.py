'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Você está ABAIXO do peso ideal!')
elif 18.5 <= imc < 25:
    print('Você está com o peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está SOBREPESO, procure um médico.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE, procure um médico.')
else: 
    print('Você está com Obesidade Mórbida, procure um médico urgente')
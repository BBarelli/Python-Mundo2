# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um polidromo,
#  desconsiderando os espaços 

frase = str(input('Digite aqui sua frase: ')).strip().upper()
palavra = frase.split() #utilizando o slip pra separa as palavras
junto = ''.join(palavra) #utilizando o join pra juntar as palavas
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palidromo')
else:
    print('Não é um palidromo')
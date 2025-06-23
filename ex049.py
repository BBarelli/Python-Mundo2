# Exercício Python 49: Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolha, só que agora utilizando um laço for

n = int(input('Digite o número que você deseja saber a tabuada: '))
for c in range(1 , 11):
    m = n * c
    print(f'{n} * {c}: {m}')
print('FIM')
#  print(f' Tabuada do {n}: {m}')
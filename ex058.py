# Exercício Python 58:Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.


from random import randint
pc = randint(0, 10)
print('Olá vamos jogar o jogo da advinhação? pensei em algum número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpite = 0

#O laço enquanto não acertou
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais..Tente novamente')
        if jogador > pc:
            print('Menos..Tente novamente')
print(f'Certa resposta eu tinha escolhido o número {pc} e com apenas {palpite} palpites você acertou ')
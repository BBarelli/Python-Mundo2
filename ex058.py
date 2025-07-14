# Exercício Python 58:Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.


from random import randint
pc = randint(0, 10)
print('Sou seu computador e acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')

acertou = False

while not acertou:
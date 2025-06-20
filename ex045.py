# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
import time

print('Vamos uma rodada de JOKEPÔ?')
print('-'*50)
print('Opções: [0. Pedra] / [1. Papel] / [2.Tesoura]')
print('-'*50)
jogador = int(input('Digite sua opção: '))
print(' ')

print('Vamos começar...')

time.sleep(1)
print('JO')
time.sleep(1)
print('KE')
time.sleep(1)
print('PÔ')
time.sleep(1)
print('-'*30)

# jogadas
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'O computador escolheu: {itens[computador]}')
print(f'E você escolheu: {itens[jogador]}')

# condições:
if computador == 0:  # Jogada do computador
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')

elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
else:
    print('Jogada Inválida')

# Exercício Python 46: Faça um programa que mostre uma contagem regressiva para a queima de fogos indo de 10 a 0
# com uma pausa de 1 segundo
import time

print('ATENÇÃO A CONTAGEM REGRESSIVA  PARA O ANO DE 2026 IRÁ COMECAR EM BREVE!!!')
print('Conte comigo......')
print(' ')

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(' ')
print('!!! FELIZ 2026 !!!!')
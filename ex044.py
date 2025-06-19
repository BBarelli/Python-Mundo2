'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros'''
import time

preco = float(input('Informe o valor do produto: '))
print('Abaixo veja as formas de pagamento:')
print('
1. A vista no dinheiro ou cheque
2. A vista no cartão 
3. 2x Cartão
4. 3x no cartão + juros')
pagamento = int(input('Qual a opção de pagamento: '))
time.sleep(1)

if pagamento == 1:
    avista = preco - (preco * 10 / 100)
    print(f'O valor a ser pago é de: {avista:.2f}')
elif pagamento == 2:
    vcartao = preco - (preco * 5 / 100)
    print(f'O valor a ser pago é de: {vcartao:.2f}')
elif pagamento == 3:
    dxcartao = preco / 2
    print(f'O valor será pago em 2 parcelas de: {dxcartao:.2f}')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas minimo 3: '))
    if parcelas < 3:
        print('Quantidade de parcelas não permitida.')
    else:
        txcartao = preco + (preco * 20 / 100)
        print(f'Em {parcelas} parcelas, o valor ficará em: {txcartao / parcelas:.2f}')
else:
    print('Forma de pagamento inválida')

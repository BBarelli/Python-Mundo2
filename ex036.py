# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual valor da casa: R$ '))
salario = float(input('Qual o valor do seu salario: R$ '))
ano = int(input('Em quantos pretende simular: '))
prestacao = casa / (ano * 12) 
limite = salario * 0.3

if prestacao <= limite:  
    print(f'O imovél no valor de:R$ {casa:.2f}, terá uma parcela de R$ {prestacao:.2f} dentro do prazo {ano} anos')    
    print('Parabéns temos margem de crédito pra você.')
else: #No else não se passa condição:    
    print(f'O imovél no valor de:R$ {casa:.2f}, terá uma parcela de R$ {prestacao:.2f} dentro do prazo {ano} anos')    
    print('Infelizmente a margem de crédito não foi liberada.')
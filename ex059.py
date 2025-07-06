# Exercício Python 59: Crie um programa que leia valores e mostre um menu na tela:
# 1.somar/2.multiplicar/3.maior/4.novos números/5.sair do programa



print('Iremos iniciar o processamento do cálculo')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

escolha = 0

while escolha != 5:
    print('''
        ===MENU===
        1. Somar,
        2.Multiplicar,
        3.Maior,
        4.Novos Números,
        5.Sair
        ''')
    
    escolha = int(input('Escolha uma opção: '))
    
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre os valores é de: {soma}')
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação dos valores é de: {multiplicar}')
    elif escolha == 3:
        if n1 > n2:
           print(f'{n1} é o maior número')
        elif n2 < n1:
           print(f'{n2} é o menor número')
        else:
            print('Os números são iguais')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('saindo')
    else:
        print('Digite novamente')
print('Obrigado por participar')
print('FIM')


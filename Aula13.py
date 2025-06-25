# Estrutura de controle: Laços, Repetições e Iteração (Laços de Repetição 1)

'''

1.Situação
Port: 
'laço' c 'no' 'intervalo'(1,10)

Python:
'for' c 'in' 'range'(1,10):
'para' c ->(váriavel de controle, pode ter o nome que vc quiser) 'no' 'intervalo
----------------------------------
2.Situação
Port:
passo
pula
passo
pula
passo
pula
passo
pega

Python: 
for c in range(0,3):
    passo
    pula
passo
pega
----------------------------------
3.Situação
Python
for c in range(0,3):
    if 'moeda':
    pega
passo
pega
'''
# CUIDADO COM A INDENTAÇÃO
# Correto
for c in range(0, 6):
    print('Oi')
print('FIM')
print(' ')

# Errado
for c in range(0, 6):
    print('Oi')
    print('FIM')
print(' ')
'''
--------------------------
'''

# Contando até 6, lembrando sempre que ele não contabiliza o último número.(7)
for c in range(1, 7):
    print(c)
print('fim')
print(' ')

# Se quiser contar em forma decresente?
for c in range(6, 0, -1):  # Aplicando a 'ITERAÇÃO', inicia no 6 executa o laço e tira 1
    print(c)
print('fim')
print(' ')

# Realizando a contagem pulando de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('fim')
print(' ')

# Ler um valor e utilizar ele dentro do 'for'
n = int(input('Digite um valor: '))
for c in range(0, n):  # se quiser contar até chegar no 'n' que foi digitado faça: (0, n+1)
    print(c)
print('FIM')
print(' ')

# Usuário definindo todos os valores:
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Pulo: '))

for c in range(i, f+1, p):
    print(c)
print('Fim')
print(' ')

# Informando algum dado mais de uma vez, só colocar o que vc quer detro de um 'for'
for c in range(0, 3):
    n = int(input('Digite um número: '))
print('Fim')

# Somando valores dentro ou utilizando um 'for'
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s = s + n  # ou s += n // No python é permitido
    print(f'O somatório entre os valores é de {s}')
print('Fim')

# Contabilizar valores ou quantidades e retornar um resultado
data_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {pessoa}: '))
    idade = data_atual - ano

    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f'Foi contabilizado {total_maior} pessoas maior de idade e {total_menor} pessoas menor de idade.')

# Comparar maior ou menor valor
maior_peso = 0
menor_peso = 0
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}º pessoa: '))
    if pessoa == 1:  
        maior_peso = peso  
        menor_peso = peso  
    else:
        if peso > maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso contabilizado foi de {maior_peso}kg')
print(f'O menor peso contabilizado foi de {menor_peso}kg')


#ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

'''
Python: quando você não sabe o limite
comando do é:
While 'variavel' not in 'parametro'
Enquanto váriavel não estiver em parametro

ou

While 'variavel' in 'parametro'
Enquanto variavel estiver no parametro

while not(maça):
    if chao:
        passo
    if vazio:
        pula
    if moeda:
        pega
pega'''

#Utiliazando o for quando eu sei o limite inicial e final
for c in range(1,11):
    print(c)
print('Fim')

#Quando não sabemos o final do intervalo utilizamos o while
c = 1
while c < 10:
    print (c)
    c += 1
print('Fim')

#Nesse exemplo o '0' seria o ponto final do programa
n = 1
while n =! 0:
    n = int(input('Digite seu numero: '))
    print(n)
print('Fim')

#Utilizando com string
r = 'S' #definindo a variavél inicial, não esquecendo de colocar as strings entre parenteses.
while r == 'S':
    n = int(input('Digite seu numero: '))
    r = str(input('Deseja continuar [S/N]')).upper()
print('Fim')
    
#Contando os numeros pares e impares em um intervalo:
n = 1 #váriavel inicial
par = impar = 0 #No python é possível utilizar esse método dois contadores recebendo o mesmo valor. 
while n != 0:
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Temos {par} números par e {impar} números impares.')
print('Fim')


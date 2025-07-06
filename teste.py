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
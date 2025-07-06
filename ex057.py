# Exercício Python 57:Faça um programa que leia o sexo de uma pessoa mas só aceite os valores
# M ou F,caso esteja errado peça o valor novamente até ter o valor correto


#Breno
sexo = ''
while sexo != 'M'and sexo != 'F':
    sexo = str(input('Informe seu sexo [M/F]: ')).strip()
    if sexo == 'M':
        print('Você é homem')
    elif sexo =='F':
        print('Você é mulher') 
    else:
        print('Digite novamente')
print('Fim')

#Guanabara
sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
   sexo = str(input('Digitação inválida, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} salvo com sucesso')

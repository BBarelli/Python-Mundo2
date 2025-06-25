# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

ssoma_idade = 0
mais_velho = 0
nome_velho = ''
mulher20 = 0

for pessoa in range(1, 4):
    print(f'----- {pessoa}ª Pessoa -----')
    nome = str(input('Nome: ').strip())
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    idade = int(input('Idade: '))
    ssoma_idade += idade

    if sexo == 'm':
        if idade > mais_velho:
            mais_velho = idade
            nome_velho = nome
    elif sexo == 'f' and idade < 20:
        mulher20 += 1

media = ssoma_idade / 4
print(f'\nA média de idade do grupo é de {media:.2f} anos.')
if nome_velho:
    print(f'O homem mais velho é {nome_velho} com {mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo, há {mulher20} mulher(es) com menos de 20 anos.')

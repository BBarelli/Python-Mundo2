'''
Criar estruturas condiconais aninhadas usando (if...elif)

Condição simplificada:
if carro.esquerda(): #você pode ter um if sem else e vários elif
    bloco 1
elif carro.direita(): # dentro do if pode usar quantos elif quiser. // nunca pode usar elif sem if
    bloco 2
else: #se utilizar nenhuma ou apenas 1x! 
    bloco 3

Relembrando a condição simples:
nome = str(input('Digite o seu nome: '))sr()
if nome == Breno:
    print('Nossa que nome bonito você tem')
print('Tenha um bom dia, {}!'.format(nome))

Relembrando a condição composta:
nome = str(input('Digite o seu nome: '))sr()
if nome == Breno:
    print('Nossa que nome bonito você tem')
else: 
    print('Seu nome é bem comum')
print('Tenha um bom dia, {}!'.format(nome))

Condição aninhada:
nome = str(input('Digite o seu nome: '))sr()
if nome == Breno:
    print('Nossa que nome bonito você tem')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular')
else: 
    print('Seu nome é bem comum')
print('Tenha um bom dia, {}!'.format(nome))


 '''


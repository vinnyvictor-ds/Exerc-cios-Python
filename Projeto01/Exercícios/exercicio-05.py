#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
#A média de idades do grupo
#Qual o nome do homem mais velho
#Quantas mulheres tem menos de 21 anos.


media_idade = 0
soma_idade = 0
idades_femininas = 0
pessoas = []
for c in range(0,4):
    nome = input('Nome: ')
    idade = int(input(f'Idade de {nome}: '))
    sexo = input(f'Sexo de {nome}(M/F):').upper()
    dados_pessoas = [nome,idade,sexo]
    pessoas.append(dados_pessoas)
    soma_idade = (soma_idade + dados_pessoas[1])
    media_idade = soma_idade / 4
    if (dados_pessoas[2] == 'F') and (dados_pessoas[1] < 21):
        idades_femininas = idades_femininas + 1
pessoas.sort(key=lambda p: p[1])
print('LISTA COMPLETA E ORDENADA: ')
print('-=' * 10)
print(pessoas)
print('-=' * 10)
print(f'Existem {idades_femininas} mulheres com menos de 21 anos. ')
print(f'A média das idades é: {media_idade:.2f}')
print(f'A pessoa mais velha é: {pessoas[3][0]}')

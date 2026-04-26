#Crie um programa que leia o ano de nascimento de três pessoas. No final, mostre quantas pessoas ainda não atingiram a
#maioridade e quantas já são maiores.
pessoas = []
for contador in range(0,3):
    nome = input('Nome: ')
    idade = int(input(f'Qual a idade de {nome}?'))
    dados_pessoa = [nome, idade]            #criei uma lista que guarda duas variáveis já definidas: nome, idade.
    pessoas.append(dados_pessoa)            #adicionei essa lista 'dados_pessoa' dentro da lista 'pessoas'.
maiores_idade = [pessoa[1] for pessoa in pessoas if pessoa[1] >= 18] #Utilizei list comprehension para separar pessoas >= 18 anos
menores_idade = [pessoa[1] for pessoa in pessoas if pessoa[1] < 18] #Utilizei list comprehension para separar pessoas < 18 anos
print(f'As pessoas que são maiores de idade são: {maiores_idade}')
print(f'Idades maiores que 18 anos: {maiores_idade}')
print(f'Idades menores que 18 anos: {menores_idade}')

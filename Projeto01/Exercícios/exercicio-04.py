#Faça um programa que leia o peso de três pessoas. No final, mostre qual foi o maior peso e qual foi o menor.
pesos_pessoas = []          #Criei uma lista vazia.
for c in range(0,3):
    peso = float(input('Qual seu peso? '))
    pesos_pessoas.append(peso)          #Adiciona os pesos na lista pesos_pessoas através do append.
pesos_pessoas.sort()            #Organiza os pesos com o metodo sort
print(f'O maior peso é: {pesos_pessoas[2]}')
print(f'O menor peso é: {pesos_pessoas[0]}')
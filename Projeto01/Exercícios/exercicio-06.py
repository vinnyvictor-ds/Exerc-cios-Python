#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
#novamente até ter um valor correto

while True:
    sexo = input('Digite o seu sexo: [M/F]').upper()
    if sexo != 'M' and sexo != 'F':
        continue
    else:
        break
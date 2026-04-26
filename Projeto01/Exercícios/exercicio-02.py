#Exercício 52: Crie um programa que leia um número inteiro e diga se ele é primo ou não.
try:
    verificador = 0
    numero = int(input('Digite um número para verificarmos se ele é primo: '))
    for c in range(1, numero + 1):
        if numero % c == 0:
            verificador = verificador + 1
        else:
            continue
    if verificador == 2:
        print(f'Há {verificador} divisores. Portanto, {numero} é primo.')
    else:
        print(f'Há  {verificador} divisores. Portanto, {numero} não é primo.')
except ValueError:
    print('O valor digitado pelo usuário é inválido. Tente novamente!')
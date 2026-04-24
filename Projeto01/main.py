from logging import exception
import numpy
from datetime import date

# #Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
# # idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# #alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
try:
    ano_nascimento = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    ano_alistamento = ano_nascimento + 18
    if ano_nascimento > ano_atual:
        raise Exception()
    elif idade > 18:
            print(f'Você tem {idade} anos e passou do prazo de se alistar.')
            print(f'Era pra você ter se alistado em {ano_alistamento}, há {ano_atual -ano_alistamento} anos atrás.')
    else:
        if idade == 18:
            print(f'Você tem {idade} anos e está no ano de se alistar.')
        else:
            print(f'Você ainda é muito novo para se alistar. ')
            print(f'Faltam {ano_alistamento - ano_atual} anos para você se alistar. ')
except:
    print('Número inválido')

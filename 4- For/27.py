# 27. Verificação de maior idade

# Crie um programa que leia o ano de nascimento de
# sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date

maiorIdade = 0
menorIdade = 0
anoAtual = date.today().year

for i in range(7):
    nascimentoPessoa = int(input("Digite o ano que você nasceu: "))
    idade = anoAtual - nascimentoPessoa
    if idade >= 18:
        maiorIdade+=1
    if idade <= 17:
        menorIdade+=1
print(f'Temos {maiorIdade} pessoas maiores de idade e {menorIdade} menores de idade')


# 30. Verificação de pesos

# Faça um programa que leia o peso de cinco
# pessoas. No final, mostre qual foi o
# maior e o menor peso lido.

maior_peso = 0
menor_peso = 0

for i in range(5):
    peso = int(input("Digite o peso: "))
    if i == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi {maior_peso} e o menor foi {menor_peso}')


# pesos = []

# for i in range(5):
#     peso = int(input(f"Digite o peso da pessoa: "))
#     pesos.append(peso)

# maior_peso = max(pesos)
# menor_peso = min(pesos)

# print(f'O maior peso lido foi {maior_peso}kg e o menor foi {menor_peso}kg')
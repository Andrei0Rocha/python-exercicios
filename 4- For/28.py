# 28. Soma pares

# Desenvolva um programa que leia seis
# números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor
# digitado for impar desconsidere-o.

soma = 0

for i in range(6):
    numero = int(input("Digite um numero para soma: "))
    if numero%2 == 0:
        soma = soma + numero
    else:
        continue
print(soma)
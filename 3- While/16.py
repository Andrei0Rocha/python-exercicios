# 16. Menor e maior numero

# Crie um programa que utilize um loop while
# para ler vários números inteiros digitados pelo
# usuário. Ao final da execução, o programa deve
# exibir a média de todos os valores inseridos, além
# de informar qual foi o maior e o menor número
# lido. O programa deve continuar solicitando
# números até que o usuário decida parar.

soma = 0
vezes = 0
maior = float('-inf')
menor = float('inf')
numero = int(input("Digite um numero: "))

while numero > 0:
    numero = input("Digite um numero: ")
    if numero.isnumeric():
        numero = int(numero)
        soma = soma + numero
        maior = max(maior, numero)
        menor = min(menor, numero)
        vezes+=1
    if numero == "parar" or numero == "Parar":
        media = soma / vezes
        print(f'A media dos numeros que você forneceu é igual a {media}')
        print(f'O maior numero foi {maior} e o menor foi {menor}')
        break
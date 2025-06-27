# 29. Tabuada

# Escreva um programa que use um loop for
# para imprimir a tabuada de um número
# fornecido pelo usuário (de 1 a 10).

mult = 0
numero = int(input("Escolha um numero para ver sua tabuada: "))

for i in range(10):
    mult+=1
    print(f'{numero} x {mult} = {numero*mult}')
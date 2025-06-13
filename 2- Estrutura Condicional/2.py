# Maior entre Dois Numeros

# Crie um programa que peça ao usuario para digitar dois numeros. O programa
# deve comparar os dois numeros e exibir uma mensagem indicando qual deles é o maior

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite mais um numero: "))

print(f'O maior numero é {max(n1,n2)} e o menor é {min(n1,n2)}')

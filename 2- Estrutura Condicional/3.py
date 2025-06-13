# Verificação de Par ou Ímpar

# Desenvolva um programa que solicite ao
# usuário um número inteiro. O programa
# deve verificar se o número é par ou ímpar e
# exibir o resultado.

numero = int(input("Digite um numero: "))

if numero%2 == 0:
    print(f'{numero} é um numero par')

elif numero == 0:
    print("0 é um numero par")
    
else:
    print(f'{numero} é um numero impar')
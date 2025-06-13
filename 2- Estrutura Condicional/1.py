# Verificação de Numero positivo ou negativo

# Escreva unm programa que solicite ao usuario um numero
# qualquer. O programa deve verificar se o numero é positivo ou negativo. Considere zero como sendo positivo.

numero = int(input("Digite um numero inteiro: "))

if numero < 0:
    print(f'{numero} é um numero negativo')
else:
    print(f'{numero} é um numero positivo')
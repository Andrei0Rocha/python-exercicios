# 23. Soma até limite

# Peça ao usuário para digitar um número limite.
# Use um loop while para calcular a soma de todos
# os números de 1 até o limite.


x = int(input("Escolha um numero para ver o fatorial: "))
inicioSomaLimite = x
soma = x

while True:
    soma-=1
    somaLimite = x
    x = x + soma
    somaLimite = x
    if soma == 1:
        print(f'A soma de todos os numeros até {inicioSomaLimite} é = {somaLimite}')
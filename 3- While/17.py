# 17. Fatorial

# Peça ao usuário para digitar um número
# inteiro positivo. Use um loop while para
# calcular o fatorial desse número.
# Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

x = int(input("Escolha um numero para ver o fatorial: "))
inicioFatorial = x
mult = x

while True:
    mult-=1
    fatorial = x
    x = x * mult
    fatorial = x
    if mult == 1:
        print(f'{inicioFatorial}! = {fatorial}')

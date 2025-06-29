# 18. Fibonacci

# Crie um programa que, dado um número
# positivo, calcule e imprima a sequência de
# Fibonacci até aquele número, utilizando
# um loop while.
# Exemplo:

# 0 –> 1 –> 1 –> 2 –> 3 –> 5 –> 8

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)

numero = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print('-'*30)
print(f'{t1} → {t2}', end='')
contador = 3

while contador <= numero:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    contador+=1
print(' → FIM')

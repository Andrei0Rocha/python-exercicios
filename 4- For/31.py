# 31. Numero primo

# Faça um programa que leia um número
# inteiro e diga se ele é ou não um numero
# primo.

numero = int(input("Digite um numero: "))

for i in range(2, numero):
  if numero%i==0:
    print('Não é Primo')
    break
else:
  print('É primo')
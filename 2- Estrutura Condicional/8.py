# Adivinhe o numero

# Escreva um programa que faça o
# computador “pensar” em um
# número inteiro entre 5 e 0 e
# peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

import random

numeroAleatorio = random.randint(0, 5)
print(numeroAleatorio)
chute = int(input("Adivinhe o numero aleatorio: "))

if chute == numeroAleatorio:
    print("Parabéns você acertou o numero aleatorio!")
else:
    print("Você errou o numero aleatorio!")
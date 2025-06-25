# 15. Adivinhe o número

# Melhore o exercício “adivinhe o numero”
# aleatório entre 1 e 100. Peça ao usuário para
# adivinhar o número. Use um loop while
# para continuar pedindo palpites até que o
# usuário acerte.
# Dê dicas como "maior" ou "menor" a cada

# tentativa.

import random

numeroAleatorio = random.randint(0, 100)

chute = int(input("Adivinhe o numero aleatorio: "))
if chute == numeroAleatorio:
        print("Parabéns você acertou o numero aleatorio!")
else:
    print(f'Você errou o numero aleatorio não é {chute} tente até acertar')     
    while chute != numeroAleatorio:
        chute = int(input("Adivinhe o numero aleatorio: "))
        if chute > numeroAleatorio:
            print(f'Você errou o numero aleatorio é menor que {chute}')
        else:
            print(f'Você errou o numero aleatorio é maior que {chute}')
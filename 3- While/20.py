# 20. JOKENPÔ

# Melhore o exercício do Jokenpô implementando um
# loop while para que o jogo continue rodando até que o
# jogador decida parar. Além disso, adicione um placar
# que registre e exiba o número de vitórias, derrotas e
# empates a cada rodada. Certifique-se de atualizar o
# placar corretamente dentro do loop..

# print("🪨")
# print("✂️")
# print("🧻")

import random
import time
import os

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

while True:
    jogadaMaquina = random.choice((pedra, papel, tesoura))
    jogadaUsuario = input("Escolha Pedra, Papel ou Tesoura: ").lower()
    
    if jogadaUsuario == 'papel' and jogadaMaquina == 'tesoura':
        print("Você: 🧻             Maquina: ✂️")
        print("Você...Gan!!")
        time.sleep(2)
        os.system('clear')
        print("Você...Perdeu!!")

    elif jogadaUsuario == 'pedra' and jogadaMaquina == 'papel':
        print("Você: 🪨             Maquina: 🧻")
        print("Você...Gan!!")
        time.sleep(2)
        os.system('clear')
        print("Você...Perdeu!!")
    elif jogadaUsuario == 'tesoura' and jogadaMaquina == 'pedra':
        print("Você: ✂️             Maquina: 🪨")
        print("Você...Gan!!")
        time.sleep(2)
        os.system('clear')
        print("Você...Perdeu!!")
    elif jogadaUsuario == 'papel' and jogadaMaquina == 'pedra':
        print("Você: 🧻             Maquina: 🪨")
        print("Você...Gan!!")
        time.sleep(2)
        os.system('clear')
        print("Você...Ganhou!!")
    elif jogadaUsuario == 'pedra' and jogadaMaquina == 'tesoura':
        print("Você: 🪨             Maquina: ✂️")
        print("Você...Gan!!")
        time.sleep(2)
        os.system('clear')
        print("Você...Ganhou!!")
    elif jogadaUsuario == 'tesoura' and jogadaMaquina == 'papel':
        print("Você: ✂️             Maquina: 🧻")
        print("Você...Gan!!")
        time.sleep(2)
        os.system('clear')
        print("Você...Ganhou!!")
    elif jogadaUsuario != 'pedra' or jogadaUsuario != 'papel' or jogadaUsuario != 'tesoura':
        os.system('clear')
        print("Opção invalida!! Escolha Somente Pedra, Papel ou Tesoura")
        print('-'*30)
        time.sleep(2)
        os.system('clear')
    else:
        os.system('clear')
        print("Empate")

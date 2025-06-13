# Crie um programa que faça o
# computador jogar Jokenpô com você:

import random

jogadaUsuario = int(input("Escolha pedra, papel ou tesolra. Obs: (PEDRA = 1) (PAPEL = 2) (TESOLRA = 3): "))

jogadaMaquina = random.randint(1, 3)



if jogadaUsuario == 1 and jogadaMaquina == 3:
    print("")
    print("")
    print("")
    print("Voce: Pedra!!                                                        Maquina: Tesolra!!")
    print("                                     Voce ganhou!!")
elif jogadaUsuario == 2 and jogadaMaquina == 1:
  print("")
  print("")
  print("")
  print("Voce: Papel!!                                                          Maquina: Pedra!!")
  print("                                       Voce ganhou!!")
elif jogadaUsuario == 3 and jogadaMaquina == 2:
  print("")
  print("")
  print("")
  print("Voce: Tesolra!!                                                        Maquina: Papel!!")
  print("                                       Voce ganhou!!")
elif jogadaUsuario == 1 and jogadaMaquina == 2:
  print("")
  print("")
  print("")
  print("Voce: Pedra!!                                                          Maquina: Papel!!")
  print("                                       Voce perdeu.")
elif jogadaUsuario == 2 and jogadaMaquina == 3:
  print("")
  print("")
  print("")
  print("Voce: Papel!!                                                          Maquina: Tesolra!!")
  print("                                       Voce perdeu.")
elif jogadaUsuario == 3 and jogadaMaquina == 1:
  print("")
  print("")
  print("")
  print("Voce: Tesolra!!                                                        Maquina: Pedra!!")
  print("                                       Voce perdeu.")
elif jogadaUsuario != 1 and jogadaUsuario != 2 and jogadaUsuario != 3:
  print("")
  print("")
  print("")
  print("Escolha Somente (PEDRA = 1) (PAPEL = 2) ou (TESOLRA = 3)")
else:
  print("")
  print("")
  print("")
  print("Empate")

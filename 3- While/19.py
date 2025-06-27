# 19. Validação de senha

# Crie um programa que solicite ao usuário que
# digite uma senha. Use um loop while para
# continuar pedindo a senha até que o usuário
# digite a senha correta (por exemplo, "1234").
# Limite o número de tentativas a 3. Após as 3
# tentativas, aguarde 10 segundos antes de
# permitir uma nova tentativa.

import time
import os

senha = '1234'
contador = 1

while True:
    print('-'*30)
    senhaUser = input("Digite a Senha do Usuario: ") 
    if senhaUser == senha:
        print("Login bem sucedido")  
        contador = 0
    elif contador == 3:
        print("Você estorou o numero de tentativas aguarde 3 segundos")
        contador = 0

        os.system('clear')
        print("Aguarde 10 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 9 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 8 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 7 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 6 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 5 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 4 sengundos")
        time.sleep(1)
        
        os.system('clear')
        print("Aguarde 3 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 2 sengundos")
        time.sleep(1)

        os.system('clear')
        print("Aguarde 1 sengundo")
        time.sleep(1)
        os.system('clear')
        
    contador+=1
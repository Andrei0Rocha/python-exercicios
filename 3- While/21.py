# 21. Cadastro

# Crie um programa que leia a idade e o sexo de
# varias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer ou
# não continuar. No final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

quantHomem = 0
quantMulher = 0
maiorIdade = 0
quantPessoas = 0
mulherVinteMenos = 0
idadeHomem = 0

while True:
    continuar = input("Deseja parar ou continuar? ").strip().lower()

    if continuar == 'continuar':
        print("Ok vamos prosseguir!")
    
    if continuar != 'parar' and continuar != 'continuar':
        print("Digite somente, parar ou continuar. ")

    if continuar == 'parar':
        print(f'Foram cadastrados {maiorIdade} pessoas com mais de 18 anos, {quantHomem} homens e {mulherVinteMenos-1} mulheres com menos de vinte anos')
        break

    sexo = input("Você é homem ou mulher? : ").strip().lower()

    if sexo == 'homem':
        quantHomem+=1
        quantPessoas+=1
        idadeHomem = int(input("Qual sua idade? "))

    if sexo == 'mulher':
        quantMulher+=1
        quantPessoas+=1
        idadeMulher = int(input("Qual sua idade? "))

    if idadeMulher < 20:
        mulherVinteMenos+=1

    if idadeHomem >= 18:
        maiorIdade+=1
    


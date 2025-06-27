# 22. caixa eletrônico

# Crie um programa que simule o funcionamento
# de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de
# R$ 50, R$ 20, R$ 10 e R$ 1.


cedulasCinquenta = 0
cedulasVinte = 0 
cedulasDez = 0
cedulasUm = 0
valorDoSaque = int(input("Digite quanto você deseja sacar: "))
while True:
    
    if valorDoSaque >= 50:
        valorDoSaque = valorDoSaque - 50
        cedulasCinquenta+=1
    if valorDoSaque >= 20:
        valorDoSaque = valorDoSaque - 20
        cedulasVinte+=1
    if valorDoSaque >= 10:
        valorDoSaque = valorDoSaque - 10
        cedulasDez+=1
    if valorDoSaque >= 1:
        valorDoSaque = valorDoSaque - 1
        cedulasUm+=1
    if valorDoSaque <= 0:
        print(f'Você acaba de sacar {cedulasCinquenta} cedulas de R$ 50, {cedulasVinte} cedulas de R$ 20, {cedulasDez} cedulas de R$ 10 e {cedulasUm} moedas de R$ 1')
        break
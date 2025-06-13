# Verificação de Ano Bissexto

# Crie um programa que peça ao usuário
# para digitar um ano. O programa deve
# verificar se o ano é bissexto e exibir uma

# mensagem informando o resultado.

ano = int(input("Digite um ano: "))

if ano % 400  == 0:
    print(f'{ano} é um ano bissexto')

elif ano % 100 == 0:
    print(f'{ano} não é um ano bissexto') 

elif ano % 4 == 0:
    print(f'{ano} é um ano bissexto')

else:
    print(f'{ano} não é um ano bissexto')

# Por que essa ordem funciona?

#     400 primeiro: todo ano divisível por 400 é bissexto (ex: 1600, 2000)

#     100 depois: anos divisíveis por 100 mas não por 400 não são bissextos (ex: 1700, 1800)

#     4 por último: anos divisíveis por 4 e não por 100 são bissextos (ex: 2024, 2020)

#     Senão, é normal


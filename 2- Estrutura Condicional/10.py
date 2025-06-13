# A confederação Nacional de Natação
# precisa de um programa que leia
# o ano de nascimento de um atleta e mostre
# sua categoria, de acordo
# com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER

idade = int(input("Digite a idade do seu atleta: "))

if idade <= 9:
    print("Seu atleta é da categoria MIRIM")
elif idade > 9 and idade <= 14:
    print("Seu atleta é da categoria INFANTIL")
elif idade > 14 and idade <= 19:
    print("Seu atleta é da categoria JUNIOR")
elif idade > 19 and idade <= 24:
    print("Seu atleta é da categoria SÊNIOR")
else:
    print("Seu atleta é da categoria MASTER")

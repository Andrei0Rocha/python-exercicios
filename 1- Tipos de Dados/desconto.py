# Desconto

# Solicite o preço original de um produto e o percentual de desconto

# Calcule o valor do desconto e o preço final

# Exiba os resultados

preco = int(input("Qual o preço do produto? "))
percentualDesconto = int(input("Qual o percentual de desconto? "))

desconto = (percentualDesconto / 100) * preco
print(f'Você terá R$ {desconto} de desconto, tendo que pagar no final R$ {preco - desconto}')
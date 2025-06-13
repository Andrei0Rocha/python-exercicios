# Classificação de Triângulos

# Escreva um programa que peça ao usuário para digitar os três
# lados de um triângulo. O programa deve verificar se os valores
# fornecidos podem formar um triângulo válido. Para que um
# triângulo seja válido, a soma de quaisquer dois lados deve ser
# maior que o terceiro lado. Se for válido, exiba "É um triângulo
# válido." Caso contrário, exiba "Não é um triângulo válido."
# Dica:
# Você precisará verificar três condições:
# Lado1 + Lado2 > Lado3
# Lado1 + Lado3 > Lado2
# Lado2 + Lado3 > Lado1

l1 = int(input("Escolha um valor para o lado 1 do triangulo: "))
l2 = int(input("Escolha um valor para o lado 2 do triangulo: "))
l3 = int(input("Escolha um valor para o lado 3 do triangulo: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
  print("É um trinagulo valido")
else:
  print("Não é um triangulo valido")

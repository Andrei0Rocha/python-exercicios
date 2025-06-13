# Peça ao usuário para inserir três valores
# representando os lados de um triângulo.
# Verifique se esses valores podem formar
# triângulo e, se sim, classifique-o c o m o

# -equilátero
# -isósceles
# -escaleno.

l1 = int(input("Escolha um valor para o lado 1 do triangulo: "))
l2 = int(input("Escolha um valor para o lado 2 do triangulo: "))
l3 = int(input("Escolha um valor para o lado 3 do triangulo: "))

if l1 == l2 and l2 == l3:
    print("Esse triangulo é Equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("E um triangulo Isósceles")
else:
    print("É um triangulo Escaleno")

#  1. Triângulo Equilátero

#     Todos os lados têm a mesma medida.

# 2. Triângulo Isósceles

#     Dois lados têm a mesma medida e o outro é diferente.

# 3. Triângulo Escaleno

#     Todos os lados têm medidas diferentes.
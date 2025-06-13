# Classificação de Salário:

# Classifique-o em:
# Baixa renda: (até R$1500)
# Média renda: (R$1500 a R$5000)
# Alta renda: (R$5000 a R10000)
# Renda muito alta:(acima de R$10000)).

renda = float(input("Indique no campo abaixo sua renda: "))

if renda <= 1500:
  print("Voce é uma pessoa de baixa renda")
elif renda > 1500 and renda <= 5000:
  print("Voce é uma pessoa de renda media")
elif renda > 5000 and renda <= 10000:
  print("Voce é uma pesoa de renda alta")
else:
  print("Voce é uma pessoa de renda muito alta")


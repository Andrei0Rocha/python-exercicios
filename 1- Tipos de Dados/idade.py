# Idade:

# Solicite o ano de nascimento.

# Calcule a idade considerando o ano atual (use a função
# datetime.now() do módulo datetime).

# Exiba a idade.

from datetime import date


nascimentoUser = int(input("Digite o ano que você nasceu: "))
anoAtual = date.today().year
idade = anoAtual - nascimentoUser
print(f'Você tem {idade} anos')

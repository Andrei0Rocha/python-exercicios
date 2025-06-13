# Verificação de Idade

# Crie um programa que solicite ao usuário
# sua idade. O programa deve verificar se o
# usuário é maior de idade (18 anos ou mais) e
# exibir uma mensagem apropriada.

idadeUsuario = int(input("Digite sua idade: "))

if idadeUsuario >= 18:
    print(f'Você é maior de idade')
elif idadeUsuario < 18:
    print("Você é menor de idade")

# Verificação de Usuário e Senha

# Escreva um programa que peça ao usuário para
# digitar um nome de usuário e uma senha. O
# programa deve verificar se o nome de usuário
# corresponde a "admin" e se a senha corresponde
# a "python123". Se ambos estiverem corretos, exiba
# a mensagem "Login bem-sucedido!". Caso
# contrário, exiba "Usuário ou senha incorretos.".

usuario = "admin"
senha = "python123"

usuarioTentativa = input("Digite o usuario: ")
senhaTentativa = input("Digite a senha: ")

if usuarioTentativa  == usuario and senhaTentativa == senha:
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos")

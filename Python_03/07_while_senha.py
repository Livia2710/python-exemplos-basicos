# Reset contador e limite de tentativas
i = 1
while i <= 3:
    user = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    # Checagem
    if user != "Gisele" or senha != "123":
        print("Usuário ou Senha Incorreto!")
        print(" ")
        i += 1
    else:
        print(" ")
        print(f"Bem-Vindo, {user}!")
        break
else:
    print(f"Você execedeu todas as: {i-1} tentativas !!")
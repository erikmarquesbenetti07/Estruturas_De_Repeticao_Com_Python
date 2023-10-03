while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if nome_usuario != senha:
        print("Usuário registrado com sucesso!")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")

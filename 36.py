# Solicite ao usuário o número para a tabuada
numero = int(input("Montar a tabuada de: "))

# Solicite ao usuário o valor inicial e final para a tabuada
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

# Verifique se o usuário digitou um valor final menor que o inicial
if fim < inicio:
    print("O valor final deve ser maior ou igual ao valor inicial.")
else:
    print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")

    # Use um loop for para gerar a tabuada
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

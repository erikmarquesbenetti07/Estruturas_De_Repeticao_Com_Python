# Solicite ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifique se o número é menor ou igual a 1
if numero <= 1:
    print("Número não é primo.")
else:
    primo = True

    # Verifique se o número é divisível por algum número de 2 até a sua raiz quadrada
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    # Se primo for True após o loop, o número é primo
    if primo:
        print("Número é primo.")
    else:
        print("Número não é primo.")

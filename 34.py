# Solicite ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicialize uma variável para verificar se o número é primo
e_primo = True

# Verifique se o número é menor ou igual a 1
if numero <= 1:
    e_primo = False
else:
    # Verifique se o número é divisível por algum número de 2 até a sua raiz quadrada
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            e_primo = False
            break

# Imprima o resultado
if e_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

# Solicite ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Verifique se o número é não negativo
if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    fatorial = 1

    # Calcule o fatorial usando um loop for
    for i in range(1, numero + 1):
        fatorial *= i

    # Imprima o resultado
    print(f"{numero}! = {fatorial}")

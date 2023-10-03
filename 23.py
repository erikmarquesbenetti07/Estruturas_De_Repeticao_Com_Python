# Solicite ao usuário que insira um número inteiro N
N = int(input("Digite um número inteiro N: "))

# Inicialize uma lista para armazenar os números primos
primos = []

# Inicialize uma variável para contar o número de divisões
num_divisoes = 0

# Verifique os números de 2 até N
for numero in range(2, N + 1):
    primo = True

    # Verifique se o número é divisível por algum número de 2 até sua raiz quadrada
    for divisor in range(2, int(numero**0.5) + 1):
        num_divisoes += 1
        if numero % divisor == 0:
            primo = False
            break

    # Se o número for primo, adicione-o à lista de primos
    if primo:
        primos.append(numero)

# Imprima os números primos encontrados
print(f"Números primos entre 1 e {N}:")
print(primos)

# Imprima o número de divisões realizadas
print(f"Número de divisões executadas: {num_divisoes}")

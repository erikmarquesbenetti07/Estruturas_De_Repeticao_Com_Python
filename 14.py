# Inicialize as variáveis para contar números pares e ímpares
numeros_pares = 0
numeros_impares = 0

# Peça ao usuário que insira 10 números inteiros
for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    
    # Verifique se o número é par ou ímpar e atualize as variáveis apropriadas
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

# Mostre a quantidade de números pares e ímpares
print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")

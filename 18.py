# Solicite ao usuário a quantidade de números que deseja inserir
n = int(input("Quantos números você deseja inserir? "))

# Verifique se n é um número positivo
if n <= 0:
    print("Por favor, insira um número positivo.")
else:
    # Inicialize variáveis para armazenar o menor valor, o maior valor e a soma
    menor_valor = float("inf")  # Inicialize com um valor infinitamente grande
    maior_valor = float("-inf")  # Inicialize com um valor infinitamente pequeno
    soma = 0

    # Solicite ao usuário que insira os números e faça os cálculos
    for i in range(n):
        numero = float(input(f"Digite o {i + 1}º número: "))
        soma += numero
        if numero < menor_valor:
            menor_valor = numero
        if numero > maior_valor:
            maior_valor = numero

    # Imprima os resultados
    print(f"Menor valor: {menor_valor}")
    print(f"Maior valor: {maior_valor}")
    print(f"Soma dos valores: {soma}")

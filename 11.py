# Solicite ao usuário que insira dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Determine o valor mínimo e máximo para o intervalo
valor_minimo = min(numero1, numero2)
valor_maximo = max(numero1, numero2)

# Inicialize a variável para a soma
soma = 0

# Use um loop for para gerar e imprimir os números no intervalo
print(f"Números no intervalo entre {valor_minimo} e {valor_maximo}:")
for numero in range(valor_minimo, valor_maximo + 1):
    print(numero)
    soma += numero

# Imprima a soma dos números no final
print(f"A soma dos números no intervalo é: {soma}")

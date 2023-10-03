n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))

# Inicialize os dois primeiros termos da série
a, b = 1, 1

# Verifique se n é menor ou igual a 0
if n <= 0:
    print("N deve ser um número positivo.")
else:
    print("Série de Fibonacci até o", n, "-ésimo termo:")
    print(a)  # Imprime o primeiro termo

    # Use um loop para gerar os próximos termos
    for i in range(2, n):
        a, b = b, a + b  # Calcule o próximo termo
        print(b)  # Imprime o próximo termo

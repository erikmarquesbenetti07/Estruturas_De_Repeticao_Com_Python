# Solicite ao usuário que insira a quantidade de notas
n = int(input("Quantas notas você deseja calcular a média? "))

# Verifique se n é um número positivo
if n <= 0:
    print("Por favor, insira um número positivo.")
else:
    # Inicialize a variável para armazenar a soma das notas
    soma = 0

    # Solicite ao usuário que insira as notas e faça a soma
    for i in range(1, n + 1):
        nota = float(input(f"Digite a {i}ª nota: "))
        soma += nota

    # Calcule a média
    media = soma / n

    # Imprima a média
    print(f"A média das {n} notas é: {media:.2f}")

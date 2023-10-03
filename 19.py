# Solicite ao usuário a quantidade de números que deseja inserir
n = int(input("Quantos números você deseja inserir? "))

# Verifique se n é um número positivo
if n <= 0:
    print("Por favor, insira um número positivo.")
else:
    # Inicialize variáveis para armazenar o menor valor, o maior valor e a soma
    menor_valor = 1001  # Inicialize com um valor maior do que o limite superior (1000)
    maior_valor = -1    # Inicialize com um valor menor do que o limite inferior (0)
    soma = 0

    # Solicite ao usuário que insira os números e faça os cálculos
    for i in range(n):
        numero = float(input(f"Digite o {i + 1}º número entre 0 e 1000: "))
        if 0 <= numero <= 1000:
            soma += numero
            if numero < menor_valor:
                menor_valor = numero
            if numero > maior_valor:
                maior_valor = numero
        else:
            print("Número fora do intervalo permitido (0 a 1000).")

    # Imprima os resultados
    print(f"Menor valor: {menor_valor}")
    print(f"Maior valor: {maior_valor}")
    print(f"Soma dos valores: {soma}")

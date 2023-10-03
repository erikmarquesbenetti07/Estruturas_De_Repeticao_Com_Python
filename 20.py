while True:
    # Solicite ao usuário que insira um número inteiro positivo e menor que 16
    n = int(input("Digite um número inteiro positivo menor que 16 para calcular o fatorial (ou um número negativo para sair): "))
    
    # Verifique se o usuário deseja sair
    if n < 0:
        break
    
    # Verifique se n está dentro dos limites permitidos
    if n < 16:
        fatorial = 1

        # Calcule o fatorial usando um loop for
        for i in range(1, n + 1):
            fatorial *= i

        # Imprima o resultado
        print(f"{n}! = {fatorial}")
    else:
        print("Número fora do intervalo permitido (0 a 15). Tente novamente.")

print("Programa encerrado.")

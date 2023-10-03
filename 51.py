n = int(input("Digite o valor de n: "))
soma = 0
numerador = 1
denominador = 1

for i in range(1, n + 1):
    termo = numerador / denominador
    soma += termo
    print(f"{numerador}/{denominador}", end=" ")
    
    # Atualize o numerador e o denominador para o próximo termo
    numerador += 1
    denominador += 2

print(f"\nSoma da série: {soma:.2f}")

soma = 0

# Solicite ao usuário que insira 5 números
for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 5

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")

# Solicite ao usuário que insira a base e o expoente
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

# Calcule a potência usando um loop for
for _ in range(expoente):
    resultado *= base

# Imprima o resultado
print(f"{base} elevado a {expoente} é igual a {resultado}")

# Inicialize uma variável para armazenar o maior número com um valor inicial baixo
maior_numero = float("-inf")

# Solicite ao usuário que insira 5 números
for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    
    # Verifique se o número é maior que o maior número atual
    if numero > maior_numero:
        maior_numero = numero

# Após o loop, imprima o maior número
print(f"O maior número é: {maior_numero}")

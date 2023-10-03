# Solicite ao usuário que insira um número inteiro
limite_superior = int(input("Digite um número inteiro: "))

# Inicialize uma lista para armazenar os números primos
numeros_primos = []

# Verifique os números de 2 até o limite superior
for numero in range(2, limite_superior + 1):
    e_primo = True
    
    # Verifique se o número é divisível por algum número de 2 até a sua raiz quadrada
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            e_primo = False
            break
    
    # Se o número for primo, adicione-o à lista
    if e_primo:
        numeros_primos.append(numero)

# Imprima a lista de números primos
print("Números primos entre 1 e", limite_superior, "são:", numeros_primos)

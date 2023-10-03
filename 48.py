# Solicite ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifique se o número é positivo
if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Converta o número em uma string para facilitar a inversão
    numero_str = str(numero)
    
    # Inverta a string
    numero_invertido_str = numero_str[::-1]
    
    # Converta a string invertida de volta para um número inteiro
    numero_invertido = int(numero_invertido_str)
    
    # Imprima o número invertido
    print(f"Número invertido: {numero_invertido}")

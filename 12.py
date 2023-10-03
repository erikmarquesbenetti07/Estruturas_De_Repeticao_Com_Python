# Solicite ao usuário que insira um número inteiro de 1 a 10
numero = int(input("Digite um número inteiro de 1 a 10 para ver a tabuada: "))

# Verifique se o número está dentro do intervalo válido
if numero < 1 or numero > 10:
    print("Número fora do intervalo válido (1 a 10).")
else:
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

# Inicialize variáveis para armazenar informações sobre os clientes
codigo_mais_alto = None
codigo_mais_baixo = None
codigo_mais_gordo = None
codigo_mais_magro = None
altura_mais_alto = float('-inf')
altura_mais_baixo = float('inf')
peso_mais_gordo = float('-inf')
peso_mais_magro = float('inf')
soma_alturas = 0
soma_pesos = 0
contador_clientes = 0

while True:
    # Solicite ao usuário que insira o código do cliente
    codigo = int(input("Digite o código do cliente (ou 0 para encerrar): "))

    # Verifique se o usuário deseja encerrar o programa
    if codigo == 0:
        break

    # Solicite ao usuário que insira a altura e o peso do cliente
    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em quilogramas): "))

    # Atualize as informações do cliente mais alto, mais baixo, mais gordo e mais magro
    if altura > altura_mais_alto:
        altura_mais_alto = altura
        codigo_mais_alto = codigo
    if altura < altura_mais_baixo:
        altura_mais_baixo = altura
        codigo_mais_baixo = codigo
    if peso > peso_mais_gordo:
        peso_mais_gordo = peso
        codigo_mais_gordo = codigo
    if peso < peso_mais_magro:
        peso_mais_magro = peso
        codigo_mais_magro = codigo

    # Atualize a soma das alturas, pesos e o contador de clientes
    soma_alturas += altura
    soma_pesos += peso
    contador_clientes += 1

# Calcule a média das alturas e dos pesos
if contador_clientes > 0:
    media_alturas = soma_alturas / contador_clientes
    media_pesos = soma_pesos / contador_clientes
else:
    media_alturas = 0
    media_pesos = 0

# Imprima as informações
print(f"Código do cliente mais alto: {codigo_mais_alto}, Altura: {altura_mais_alto} metros")
print(f"Código do cliente mais baixo: {codigo_mais_baixo}, Altura: {altura_mais_baixo} metros")
print(f"Código do cliente mais gordo: {codigo_mais_gordo}, Peso: {peso_mais_gordo} kg")
print(f"Código do cliente mais magro: {codigo_mais_magro}, Peso: {peso_mais_magro} kg")
print(f"Média das alturas: {media_alturas:.2f} metros")
print(f"Média dos pesos: {media_pesos:.2f} kg")

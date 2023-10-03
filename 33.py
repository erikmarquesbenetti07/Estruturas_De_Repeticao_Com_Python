# Inicialize variáveis para a menor e a maior temperatura e a soma das temperaturas
menor_temperatura = float('inf')  # Inicialize com um valor infinito positivo
maior_temperatura = float('-inf')  # Inicialize com um valor infinito negativo
soma_temperaturas = 0
contador = 0

while True:
    # Solicite ao usuário que insira a temperatura
    temperatura = input("Digite a temperatura (ou 'fim' para encerrar): ")

    # Verifique se o usuário deseja encerrar o programa
    if temperatura.lower() == 'fim':
        break

    # Converta a entrada em um número de ponto flutuante
    try:
        temperatura = float(temperatura)
    except ValueError:
        print("Entrada inválida. Insira um número válido ou 'fim'.")
        continue

    # Atualize a menor e a maior temperatura
    menor_temperatura = min(menor_temperatura, temperatura)
    maior_temperatura = max(maior_temperatura, temperatura)

    # Adicione a temperatura à soma
    soma_temperaturas += temperatura

    # Incremente o contador
    contador += 1

# Verifique se foram inseridas temperaturas antes de calcular a média
if contador > 0:
    media_temperaturas = soma_temperaturas / contador
    print(f"Menor temperatura: {menor_temperatura:.2f}°C")
    print(f"Maior temperatura: {maior_temperatura:.2f}°C")
    print(f"Média das temperaturas: {media_temperaturas:.2f}°C")
else:
    print("Nenhuma temperatura foi inserida.")

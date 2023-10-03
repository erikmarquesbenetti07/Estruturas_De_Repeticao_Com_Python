# Inicialize contadores para cada intervalo
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    # Solicite ao usuário que insira um número
    numero = int(input("Digite um número positivo (ou negativo para encerrar): "))
    
    # Verifique se o número é negativo para encerrar o programa
    if numero < 0:
        break
    
    # Classifique o número em um dos intervalos e atualize o contador apropriado
    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1

# Imprima os resultados
print("Quantidade de números nos intervalos:")
print("[0-25]:", intervalo_0_25)
print("[26-50]:", intervalo_26_50)
print("[51-75]:", intervalo_51_75)
print("[76-100]:", intervalo_76_100)

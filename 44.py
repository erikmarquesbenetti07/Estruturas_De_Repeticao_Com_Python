# Inicialize contadores para cada candidato e para votos nulos e em branco
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_em_branco = 0
total_votos = 0

# Use um loop para ler os votos até que seja digitado 0
while True:
    voto = int(input("Digite o código do candidato (1, 2, 3, 4), 5 para voto nulo, 6 para voto em branco ou 0 para encerrar: "))
    
    # Verifique se o voto é zero para encerrar a votação
    if voto == 0:
        break
    
    # Classifique o voto e atualize o contador apropriado
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1

    total_votos += 1

# Calcule as porcentagens
porcentagem_nulos = (votos_nulos / total_votos) * 100
porcentagem_branco = (votos_em_branco / total_votos) * 100

# Imprima os resultados
print("Resultados da eleição:")
print(f"Total de votos para Candidato 1: {votos_candidato1}")
print(f"Total de votos para Candidato 2: {votos_candidato2}")
print(f"Total de votos para Candidato 3: {votos_candidato3}")
print(f"Total de votos para Candidato 4: {votos_candidato4}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_em_branco}")
print(f"Percentagem de votos nulos sobre o total de votos: {porcentagem_nulos:.2f}%")
print(f"Percentagem de votos em branco sobre o total de votos: {porcentagem_branco:.2f}%")

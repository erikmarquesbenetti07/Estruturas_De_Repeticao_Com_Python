# Solicite ao usuário o número total de eleitores
num_eleitores = int(input("Digite o número total de eleitores: "))

# Inicialize as variáveis para contar os votos de cada candidato
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

# Solicite a cada eleitor que vote e conte os votos
for eleitor in range(1, num_eleitores + 1):
    print(f"Eleitor {eleitor}:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    voto = int(input("Digite o número do candidato escolhido: "))
    
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido. Por favor, escolha um candidato válido.")

# Imprima o número de votos de cada candidato
print("Resultados da eleição:")
print(f"Total de votos para o Candidato 1: {votos_candidato1}")
print(f"Total de votos para o Candidato 2: {votos_candidato2}")
print(f"Total de votos para o Candidato 3: {votos_candidato3}")

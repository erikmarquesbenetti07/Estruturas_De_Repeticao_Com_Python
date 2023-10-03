while True:
    nome_ginasta = input("Digite o nome do ginasta (ou deixe em branco para encerrar): ")
    
    if nome_ginasta == "":
        break
    
    notas = []
    
    for i in range(1, 8):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)
    
    # Encontre a melhor e a pior nota
    melhor_nota = max(notas)
    pior_nota = min(notas)
    
    # Calcule a média das notas restantes (excluindo a melhor e a pior)
    notas.remove(melhor_nota)
    notas.remove(pior_nota)
    media_notas = sum(notas) / 5
    
    # Imprima os resultados
    print(f"Atleta: {nome_ginasta}")
    print(f"Melhor nota: {melhor_nota}")
    print(f"Pior nota: {pior_nota}")
    print(f"Média: {media_notas:.2f}")
    print(f"Resultado final:")
    print(f"Atleta: {nome_ginasta}")
    print(f"Melhor nota: {melhor_nota}")
    print(f"Pior nota: {pior_nota}")
    print(f"Média: {media_notas:.2f}")

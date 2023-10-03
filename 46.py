while True:
    nome_atleta = input("Digite o nome do atleta (ou deixe em branco para encerrar): ")
    
    if nome_atleta == "":
        break
    
    saltos = []
    
    for i in range(1, 6):
        salto = float(input(f"{i}º Salto: "))
        saltos.append(salto)
    
    # Encontre o melhor e o pior salto
    melhor_salto = max(saltos)
    pior_salto = min(saltos)
    
    # Calcule a média dos demais saltos (excluindo o melhor e o pior)
    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)
    media_saltos = sum(saltos) / 3
    
    # Imprima os resultados
    print(f"Atleta: {nome_atleta}")
    print(f"Melhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")
    print(f"Média dos demais saltos: {media_saltos:.2f} m")
    print(f"Resultado final:")
    print(f"{nome_atleta}: {media_saltos:.2f} m")

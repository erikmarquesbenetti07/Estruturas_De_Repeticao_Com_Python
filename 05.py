while True:
    try:
        populacao_a = int(input("Digite a população inicial do país A: "))
        taxa_crescimento_a = float(input("Digite a taxa de crescimento anual do país A (em decimal): "))
        populacao_b = int(input("Digite a população inicial do país B: "))
        taxa_crescimento_b = float(input("Digite a taxa de crescimento anual do país B (em decimal): "))
        
        if populacao_a < 0 or populacao_b < 0 or taxa_crescimento_a <= 0 or taxa_crescimento_b <= 0:
            raise ValueError("Populações devem ser não negativas e taxas de crescimento devem ser positivas.")
        
        anos = 0

        while populacao_a < populacao_b:
            populacao_a += populacao_a * taxa_crescimento_a
            populacao_b += populacao_b * taxa_crescimento_b
            anos += 1

        print(f"Serão necessários {anos} anos para que a população de A ultrapasse a população de B.")
        
        continuar = input("Deseja calcular novamente? (S/N): ").strip().lower()
        if continuar != 's':
            break

    except ValueError as e:
        print(f"Erro: {e}")

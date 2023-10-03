while True:
    # Inicialize o total da compra
    total_compra = 0.0

    # Imprima o cabeçalho da loja
    print("Lojas Tabajara")

    # Use um loop para receber os preços das mercadorias
    produto = 1
    while True:
        preco = float(input(f"Produto {produto}: R$ "))
        if preco == 0:
            break
        total_compra += preco
        produto += 1

    # Imprima o total da compra
    print(f"Total: R$ {total_compra:.2f}")

    # Solicite o valor em dinheiro fornecido pelo cliente
    dinheiro = float(input("Dinheiro: R$ "))

    # Calcule o troco
    troco = dinheiro - total_compra

    # Imprima o valor do troco
    print(f"Troco: R$ {troco:.2f}")

    # Verifique se o cliente deseja registrar outra compra
    continuar = input("Registrar outra compra? (S/N): ")
    if continuar.lower() != "s":
        break

# Defina o cardápio como um dicionário onde as chaves são os códigos e os valores são as especificações e preços
cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

# Inicialize o total do pedido
total_pedido = 0

# Use um loop para ler os itens pedidos e suas quantidades
while True:
    codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))
    
    # Verifique se o código é zero para encerrar o pedido
    if codigo == 0:
        break
    
    # Verifique se o código é válido
    if codigo not in cardapio:
        print("Código inválido. Por favor, digite um código válido.")
        continue
    
    quantidade = int(input("Digite a quantidade desejada: "))
    
    # Calcule o valor a ser pago por item (preço * quantidade)
    especificacao, preco = cardapio[codigo]
    valor_item = preco * quantidade
    
    # Acumule o valor do item ao total do pedido
    total_pedido += valor_item
    
    # Imprima o valor a ser pago por item
    print(f"{quantidade} {especificacao}(s): R$ {valor_item:.2f}")
    
# Imprima o total geral do pedido
print(f"Total do pedido: R$ {total_pedido:.2f}")

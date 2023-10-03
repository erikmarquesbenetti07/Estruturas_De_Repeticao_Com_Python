# Imprima o cabeçalho da tabela
print("Lojas Quase Dois - Tabela de preços")

# Use um loop para gerar a tabela de preços para 1 até 50 produtos
for quantidade in range(1, 51):
    preco = quantidade * 1.99
    print(f"{quantidade} - R$ {preco:.2f}")

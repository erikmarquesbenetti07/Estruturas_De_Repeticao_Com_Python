# Solicite ao usuário o preço do pão
preco_do_pao = float(input("Digite o preço do pão: R$ "))

# Imprima o cabeçalho da tabela
print("Panificadora Pão de Ontem - Tabela de preços")

# Use um loop para gerar a tabela de preços para 1 até 50 pães
for quantidade in range(1, 51):
    valor_total = quantidade * preco_do_pao
    print(f"{quantidade} - R$ {valor_total:.2f}")

# Solicite ao usuário que insira o valor da dívida
valor_divida = float(input("Digite o valor da dívida: R$ "))

# Inicialize as taxas de juros e a quantidade de parcelas de acordo com a tabela
taxas_juros = [0, 0.10, 0.15, 0.20, 0.25]
quantidade_parcelas = [1, 3, 6, 9, 12]

# Imprima o cabeçalho da tabela
print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")

# Use um loop para calcular e imprimir os valores para cada combinação de taxa de juros e parcelas
for i in range(len(taxas_juros)):
    taxa_juros = taxas_juros[i]
    parcelas = quantidade_parcelas[i]
    
    # Calcule o valor dos juros
    valor_juros = valor_divida * taxa_juros
    
    # Calcule o valor da parcela
    valor_parcela = (valor_divida + valor_juros) / parcelas
    
    # Imprima os valores formatados
    print(f"R$ {valor_divida:.2f} | R$ {valor_juros:.2f} | {parcelas} | R$ {valor_parcela:.2f}")

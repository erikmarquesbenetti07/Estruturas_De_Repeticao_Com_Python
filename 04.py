populacao_a = 80000
taxa_crescimento_a = 0.03  # 3%

populacao_b = 200000
taxa_crescimento_b = 0.015  # 1.5%

anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população de A ultrapasse a população de B.")

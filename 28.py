# Solicite ao usuário a quantidade de CDs na coleção
num_cds = int(input("Digite a quantidade de CDs na coleção: "))

# Inicialize variáveis para o valor total e a soma dos valores dos CDs
valor_total = 0

# Use um loop for para solicitar o valor de cada CD
for i in range(1, num_cds + 1):
    valor_cd = float(input(f"Digite o valor do CD {i}: "))
    valor_total += valor_cd

# Calcule o valor médio gasto em cada CD
if num_cds > 0:
    valor_medio_por_cd = valor_total / num_cds
    print(f"O valor total investido na coleção de CDs é: R${valor_total:.2f}")
    print(f"O valor médio gasto em cada CD é: R${valor_medio_por_cd:.2f}")
else:
    print("A coleção não possui CDs.")

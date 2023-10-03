# Solicite ao usuário o número de pessoas na turma
n = int(input("Quantas pessoas na turma? "))

# Inicialize a variável para armazenar a soma das idades
soma_idades = 0

# Solicite ao usuário que insira as idades das pessoas e faça a soma
for i in range(1, n + 1):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    soma_idades += idade

# Calcule a média de idade
media_idades = soma_idades / n

# Verifique em qual faixa etária a média se encaixa
if 0 <= media_idades <= 25:
    faixa_etaria = "jovem"
elif 26 <= media_idades <= 60:
    faixa_etaria = "adulta"
else:
    faixa_etaria = "idosa"

# Imprima a média e a faixa etária
print(f"A média de idade da turma é: {media_idades:.2f} anos")
print(f"A turma é classificada como {faixa_etaria}")

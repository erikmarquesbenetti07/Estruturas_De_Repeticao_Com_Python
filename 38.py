# Solicita ao usuário o salário inicial
salario_inicial = float(input("Digite o salário inicial do funcionário: "))

# Ano inicial
ano = 1995

# Ano atual
ano_atual = 2023

# Inicializa o salário com o salário inicial fornecido pelo usuário
salario = salario_inicial

# Calcula os aumentos salariais até o ano atual
while ano <= ano_atual:
    aumento_percentual = 1.5 if ano == 1996 else aumento_percentual * 2
    salario += (aumento_percentual / 100) * salario
    ano += 1

# Imprime o salário atual
print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")

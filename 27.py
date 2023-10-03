# Solicite ao usuário a quantidade de turmas
num_turmas = int(input("Digite a quantidade de turmas: "))

# Inicialize variáveis para contar o número total de alunos e o número de turmas válidas
total_alunos = 0
turmas_validas = 0

# Use um loop for para solicitar a quantidade de alunos em cada turma
for i in range(1, num_turmas + 1):
    # Solicite ao usuário a quantidade de alunos na turma
    alunos_na_turma = int(input(f"Digite a quantidade de alunos na turma {i}: "))
    
    # Verifique se a quantidade de alunos na turma é válida (até 40)
    if 1 <= alunos_na_turma <= 40:
        total_alunos += alunos_na_turma
        turmas_validas += 1
    else:
        print("Quantidade de alunos inválida. A turma deve ter de 1 a 40 alunos.")

# Calcule o número médio de alunos por turma
if turmas_validas > 0:
    media_alunos_por_turma = total_alunos / turmas_validas
    print(f"A média de alunos por turma é: {media_alunos_por_turma:.2f}")
else:
    print("Não foram inseridas turmas válidas.")

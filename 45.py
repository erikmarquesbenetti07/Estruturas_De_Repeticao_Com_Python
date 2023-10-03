# Inicialize o gabarito da prova
gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

# Inicialize variáveis para estatísticas
maior_acerto = 0
menor_acerto = 10
total_alunos = 0
soma_notas = 0

while True:
    # Solicite ao aluno que insira as respostas
    respostas_aluno = []
    for i in range(1, 11):
        resposta = input(f"Resposta da questão {i}: ").upper()  # Converta para maiúsculas
        respostas_aluno.append(resposta)

    # Compare as respostas com o gabarito e calcule o total de acertos
    total_acertos = sum(1 for a, b in zip(respostas_aluno, gabarito) if a == b)

    # Calcule a nota (1 ponto por resposta certa)
    nota = total_acertos

    # Atualize as estatísticas
    total_alunos += 1
    soma_notas += nota
    if total_acertos > maior_acerto:
        maior_acerto = total_acertos
    if total_acertos < menor_acerto:
        menor_acerto = total_acertos

    # Imprima a nota do aluno
    print(f"Total de acertos: {total_acertos}")
    print(f"Nota: {nota}")

    # Pergunte se outro aluno vai utilizar o sistema
    continuar = input("Outro aluno vai utilizar o sistema? (S para sim, qualquer outra tecla para encerrar): ").upper()
    if continuar != "S":
        break

# Calcule a média das notas da turma
media_notas = soma_notas / total_alunos

# Imprima as estatísticas finais
print("Estatísticas finais:")
print(f"Maior acerto: {maior_acerto}")
print(f"Menor acerto: {menor_acerto}")
print(f"Total de alunos: {total_alunos}")
print(f"Média das notas da turma: {media_notas:.2f}")

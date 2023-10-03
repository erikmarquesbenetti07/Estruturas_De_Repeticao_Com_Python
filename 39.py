# Inicialize variáveis para armazenar as informações do aluno mais alto e mais baixo
numero_aluno_mais_alto = None
altura_aluno_mais_alto = float('-inf')
numero_aluno_mais_baixo = None
altura_aluno_mais_baixo = float('inf')

# Use um loop para ler as informações dos dez alunos
for i in range(1, 11):
    numero_aluno = int(input(f"Digite o número do aluno {i}: "))
    altura_aluno = float(input(f"Digite a altura do aluno {i} em centímetros: "))

    # Verifique se o aluno é o mais alto ou o mais baixo até agora
    if altura_aluno > altura_aluno_mais_alto:
        altura_aluno_mais_alto = altura_aluno
        numero_aluno_mais_alto = numero_aluno
    if altura_aluno < altura_aluno_mais_baixo:
        altura_aluno_mais_baixo = altura_aluno
        numero_aluno_mais_baixo = numero_aluno

# Imprima o número e a altura do aluno mais alto e do aluno mais baixo
print(f"Aluno mais alto: Número {numero_aluno_mais_alto}, Altura: {altura_aluno_mais_alto} cm")
print(f"Aluno mais baixo: Número {numero_aluno_mais_baixo}, Altura: {altura_aluno_mais_baixo} cm")

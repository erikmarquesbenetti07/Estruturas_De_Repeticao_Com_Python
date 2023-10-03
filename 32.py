# Solicite ao usuário um número inteiro
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicialize a variável para armazenar o fatorial
fatorial = 1

# Inicialize uma string para armazenar a representação do fatorial
representacao_fatorial = f"{numero}! ="

# Calcule o fatorial
for i in range(numero, 0, -1):
    fatorial *= i
    representacao_fatorial += f" {i} ."

# Remova o último ponto da representação
representacao_fatorial = representacao_fatorial[:-1]

# Imprima o resultado
print(f"Fatorial de: {numero}")
print(representacao_fatorial, "=", fatorial)

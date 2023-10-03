while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Nome deve ter mais de 3 caracteres. Tente novamente.")

while True:
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <= 150:
        break
    else:
        print("Idade deve estar entre 0 e 150. Tente novamente.")

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("Salário deve ser maior que zero. Tente novamente.")

while True:
    sexo = input("Digite 'f' para feminino ou 'm' para masculino: ")
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Sexo deve ser 'f' ou 'm'. Tente novamente.")

while True:
    estado_civil = input("Digite 's' para solteiro(a), 'c' para casado(a), 'v' para viúvo(a) ou 'd' para divorciado(a): ")
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente.")

print("Informações validadas com sucesso!")

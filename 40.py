# Inicialize variáveis para armazenar as informações sobre as cidades
cidade_maior_indice = None
cidade_menor_indice = None
maior_indice = float('-inf')
menor_indice = float('inf')
total_veiculos = 0
total_acidentes = 0
total_cidades_menos_2000_veiculos = 0
total_acidentes_cidades_menos_2000_veiculos = 0

# Use um loop para ler os dados das cinco cidades
for i in range(1, 6):
    codigo_cidade = int(input(f"Digite o código da cidade {i}: "))
    veiculos_1999 = int(input(f"Digite o número de veículos de passeio em 1999 na cidade {i}: "))
    acidentes_1999 = int(input(f"Digite o número de acidentes de trânsito com vítimas em 1999 na cidade {i}: "))

    # Calcule o índice de acidentes de trânsito
    indice_acidentes = acidentes_1999 / veiculos_1999

    # Atualize o maior e o menor índice de acidentes e as cidades correspondentes
    if indice_acidentes > maior_indice:
        maior_indice = indice_acidentes
        cidade_maior_indice = codigo_cidade
    if indice_acidentes < menor_indice:
        menor_indice = indice_acidentes
        cidade_menor_indice = codigo_cidade

    # Atualize as somas totais de veículos e acidentes
    total_veiculos += veiculos_1999
    total_acidentes += acidentes_1999

    # Verifique se a cidade tem menos de 2.000 veículos de passeio
    if veiculos_1999 < 2000:
        total_cidades_menos_2000_veiculos += 1
        total_acidentes_cidades_menos_2000_veiculos += acidentes_1999

# Calcule as médias
media_veiculos = total_veiculos / 5
media_acidentes_cidades_menos_2000_veiculos = total_acidentes_cidades_menos_2000_veiculos / total_cidades_menos_2000_veiculos

# Imprima os resultados
print(f"Cidade com o maior índice de acidentes: Código {cidade_maior_indice}, Índice: {maior_indice:.2f}")
print(f"Cidade com o menor índice de acidentes: Código {cidade_menor_indice}, Índice: {menor_indice:.2f}")
print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
print(f"Média de acidentes de trânsito nas cidades com menos de 2.000 veículos: {media_acidentes_cidades_menos_2000_veiculos:.2f}")

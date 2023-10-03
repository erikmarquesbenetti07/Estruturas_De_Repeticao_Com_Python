# Inicialize os dois primeiros termos da série
a, b = 0, 1

# Imprima os primeiros dois termos da série
print(a)
print(b)

# Use um loop while para gerar os próximos termos até que o valor seja maior que 500
while a + b <= 500:
    a, b = b, a + b  # Calcule o próximo termo
    print(a + b)  # Imprima o próximo termo

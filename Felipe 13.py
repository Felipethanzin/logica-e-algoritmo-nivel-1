13 - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.


# Passo 1: Ler idade em anos, meses e dias
anos = int(input("Digite a idade (anos): "))
meses = int(input("Digite os meses: "))
dias = int(input("Digite os dias: "))

# Passo 2: Calcular idade total em dias
idade_em_dias = (anos * 365) + (meses * 30) + dias

# Passo 3: Mostrar o resultado
print(f"A idade em dias é: {idade_em_dias}")

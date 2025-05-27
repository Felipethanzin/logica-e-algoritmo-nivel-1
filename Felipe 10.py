#10 -Escreva um software informe a média aritmética de um aluno que cursou 4 bimestres

#Etapas para programar

#1 - obter as 4 notas do aluno
#2 - efetuar a conta
#3 - mostrar a média aritmética




nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média aritmética do aluno é: {media:.2f}")

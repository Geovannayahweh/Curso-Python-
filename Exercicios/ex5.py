# Desempenho escolar
# O professor digita a nota e o sistema calcula de acordo: 
# Maior ou igual a 9, excelente, vc tirou um A
# Maior ou igual a 7, bom trabalho, vc tirou um B
# Maior ou igual a 5, vc passou mas precisa melhorar. Sua nota é C 
# Qualquer nota abaixo, Reprovado.

nota = float(input("Digite a nota do aluno:"))
if nota >= 9.0: 
    print("Excelente, você tirou um A")
elif nota >= 7.0: 
    print("Bom trabalho, você tirou um B")
elif nota >= 5.0:
    print("Você passou mas precisa melhorar. Sua nota foi um C")
else: 
    print("Reprovado")      
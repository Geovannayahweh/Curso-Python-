#Saudações 
# Bom dia - antes das 12:00
# Boa tarde - antes das 18:00
# Boa noite - restante 

hora = int(input("Digite o horário atual:"))
if hora <= 12:
    print("Bom dia")
elif hora >= 12 and hora <= 18:
    print("Boa tarde")
else: 
    print("Boa noite")
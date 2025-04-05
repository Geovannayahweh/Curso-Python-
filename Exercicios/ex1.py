# controle de temperaturas 
# Menor do que 10c - Esta frio 
# Menor do que 20c - Esta fresco 
# O restante - esta quente 

temperatura = int(input ("Digite a temperatura:"))
if temperatura <= 10:
    print("Ësta frio")
elif temperatura <= 20:
    print("Esta fresco")
else:
    print("Esta quente")
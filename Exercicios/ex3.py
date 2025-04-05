#Desconto 
# O usuário precisa entrar com o valor da compra 
# Compra de qualquer valor - 5% de desconto 
# Compra acima de R$100 - 10% de desconto 
# Compra acima de R$200 - 20% de desconto 

valor_total = float(input("Digite o valor total da compra:"))
desconto = 0

if valor_total > 100 and valor_total < 200:
    desconto = valor_total * 0.10
    print(f"O novo valor da compra de {valor_total} com 10% de desconto é igual a R$ {valor_total - desconto}")
elif valor_total > 200:
    desconto = valor_total * 0.20
    print(f"O novo valor da compra de {valor_total} com 20% de desconto é igual a R$ {valor_total - desconto}")
else:
    print(f"O novo valor da compra de {valor_total} com 5% de desconto é igual a R$ {valor_total - desconto}")

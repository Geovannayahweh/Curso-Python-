# Login Athentication 
# O usuario vgai ter que digitar o seu: 
# username e password

# No sistema, crie um username e password de acordo: 
# username: admin 
# password 123456

# Certo: login OK 
# Errado: Usuario ou senha incorretos

user = input("Digite seu nome de usuário:")
password = input("Digite sua senha:")

if user == "admin" and password == "123456":
    print("login OK")
else:
    print("Usuario ou senha incorretos")
# Crie m codigo python que verifique se a senha digitada 
# pelo usuario for "1234" , exiba "Acessa Permitido".

senha_certa = "1234"

senha = (input("Digite a senha: "))
if senha == senha_certa:
    print("acesso liberado")
else:
    print("Acesso negado")

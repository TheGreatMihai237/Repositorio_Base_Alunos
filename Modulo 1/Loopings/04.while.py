# crie um código que faça a conversão de moeda do real para dólar e vice-versa

# Etapas da resolução:
# 1) Criar uma variável chamada cotacao
# 2) Solicitar ao usuário a opção de conversão desejada
# 3) Apresentar o resultado da conversão de moeda
# 4) Perguntar se ele deseja continuar a conversão

letra = "s"
while letra == "s":
    cotacao = float(input("Digite a cotação do dólar: "))
    print("-"*50)
    print(f"-"*15,"Escolha a opção","-"*15)
    print("-"*50)

    opcao = int(input("1 - Converter dolar para real |  2 - conversor real para dolar: "))

    if opcao == 1:
        valor = float(input("Digite o valor em dolár a ser convertido para real u$: "))
        resultado = valor * cotacao
        print(f"O valor em reais é : {resultado:.2f}")
    elif opcao == 2:
        valor1 = float(input("Digite o valor em real desejado a ser convertido para dolár "))
        resultado1 = valor1 / cotacao
        print(f"O valor em dolár é : {resultado1:.2f}")
    else:
        print("Digite uma opção valida")
    letra = input("Deseja continuar? (s/n): ").lower()

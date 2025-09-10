#peça a usuario para digitar uma letra
#se for vogal, informe qual vogal
#se for consoante, verifique se é maiúscula ou minúscula

#solicitação de entrada
letra = input("Digite uma letra: ")

if letra.lower() in "aeiou": # .lower() transforma letras em minusculo
    print(f"Vogal: {letra}")
else:
    if letra.isupper():
        print(f"Consoante maiúscula: {letra} ")
    else:
        print(f"Consoante minúscula: {letra} ")

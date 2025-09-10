# 2. paridade e tamanho do numero 
# crie um código que receba um numero inteiro e informe:
# - se é par o impar
# - e, ao mesmo tempo, se é maior que 10 ou menor ou igual a 10
# utilize condicionais aninhadas para organizar a verificações

num = int(input("Digite um numero: "))

if num % 2==0:
    if num >= 10:
        print(f"o numero {num} é par e maior que dez")
    else:
        print(f"o numero {num} é par e menor que dez")
else:
    if num >= 10:
        print(f"o numero {num} é impar e é maior que dez ")
    else:
        print(f"o numero {num} é impar e menor que 10")
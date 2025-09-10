#3 classificação por idade 
# faça um programa que leia a idade de uma pessoa e classifique como
# criança: menor que 12 anos
# adolescente: entre 12 e 17 anos
# adulto: maior ou igual a 18 anos
# utilize a estrutura de condicional aninhada

idade = int(input("Digite sua idade: "))

if idade > 0:
    if idade >= 18:
        print(f"voce tem {idade} anos e é adulto.")
    elif 12 <= idade <=17:
        print(f"Você tem {idade} e é adolescente. ")
    else:
        print(f"Você tem {idade} e é uma criança.")
else:
    print("Idade não pode ser negativa, digite uma idade válida.")
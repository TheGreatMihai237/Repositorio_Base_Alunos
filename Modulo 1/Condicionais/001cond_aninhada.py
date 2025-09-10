# 1 indentificação de numero positivo, negativo ou zero
#crie um codigo em python que leia um numero e informe se ele
# é positivo, negativo ou zero




#1) entrada de dados
num = int(input("digite um numero inteiro: "))
#2) condicional para verificar se o numero e maior ou igual a zero
if num >= 0:
    # condicional para chegar se o numero e zero
    if num == 0:
        print("o número digitado é zero.")
    else: # informar que o numero é positivo
        print(f"O número {num} é positivo.")
#se o if for falso, entre no else e informa que o numero e negativo
else:
    print(f"O número {num} é negativo.")
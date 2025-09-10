#crie um codigo em python que peça um numero ao usuario
# e exiba "numero par" se ele for divisivel por 2.

#etapas de resolução

# 1) solicitar um numero ao usuario
# 2) verificar se o numero é par ou impar
# 3) informar se o número é par ou impar


numero = float(input("Digite um número "))

if numero %2 == 0:
    print(f"O número {numero} é par ")
else:
    print(f"O número {numero} é impar ")
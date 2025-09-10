                                                                #tipo de triangulo
#crie um programa que receba três lados de um triângulo
#verifique se os lados realmente podem formar um triângulo
# e determine os triângulos em:
#Equilatero (todos os lados são iguais)
#Isósceles (dois lados iguais)
#Escaleno (todos os lados diferentes)

a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

# Verficar se os lados formam um triangulo
if a + b > c and a + c > b and b + c > a: # condicação pra formação do triangulo
    if a == b: 
        if b == c:
            print(f"Os lados do triangulo são {a}, {b} e {c}: Triângulo Equilátero")
        else:
            print(f"Os lados do triangulo são {a}, {b} e {c}: Triângulo Isósceles")
    else: # não é possivel formar um triangulo
        if b == c or a == c:
            print(f"Os lados do triangulo são {a}, {b} e {c}: Triângulo Isosceles")
        else:
            print(f"Os lados do triangulo são {a}, {b} e {c}: Triangulo Escaleno")
else:
    print("Os lados ão formam um triângulo valido.")
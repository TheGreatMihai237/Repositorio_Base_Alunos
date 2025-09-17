# crie um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lido.


# etapas para resolução:

# 1) crie uma lista vazia para receber os pesos
# 2) crie um for para receber os pesos das 5 pessoas.
# 3) adiciona os pesos recebidos a lista
# 4) utilize a função max() e min() ou ordene a lista e busque o primeiro e o ultimo
# elemento
# 5) apresente os resultados

pesos = []

for i in range(5):
    peso = float(input(f"informe o peso da {i+1} pessoa: "))
    if peso > 0:
        pesos.append(peso)
else:
    print("Valor inválido.")

#pode ser também
# menor_peso = pesos.max()
# maior_peso = pesos.min()
# print(f"o maior peso é {maior_peso} e o menor peso é {menor}Kg.")

pesos.sort()
menor =pesos[0]
maior = pesos[-1]

print(f"o maior peso é {maior} Kg e o menor peso é {menor} Kg.")
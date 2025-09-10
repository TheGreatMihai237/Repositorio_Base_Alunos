# copy()
# Dada a lista original = [1, 2, 3, 4], use .copy() para criar
# uma nova lista
# chamada copia. Altere a copia (adicione o número 99)
#  e mostre as duas listas
# para verificar que são independentes.

lista_original = [1, 2, 3, 4]
print(f"lista original: {lista_original}")

lista_copia = lista_original.copy()
print(f"lista copia:{lista_copia}")

lista_copia.append(99)
print(f"lista copia após o append:{lista_copia}")
print(lista_copia)

# dada a lista numeros = [1, 2, 3], use .extend()
#para adicionar os elementos de outra 
#lista mais-numeros = [4, 5, 6].
#mostre o resultado

numeros = [1, 2, 3]
print(numeros)

novos_numeros = [4, 5, 6] # nova variavel
#recebe uma lista

numeros.extend(novos_numeros) # extende a lista numeros
print(numeros)
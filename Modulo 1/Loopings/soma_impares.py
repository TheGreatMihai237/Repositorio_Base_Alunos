# Crie um programa que some todos os números ímpares 
# que são multiplos de 3 e 1 a 30 e apresente o resultado

# Etapas para resolução:
# 1) criar um for de para captar os números ímpares
# 2) criar uma condicional para checar se o número é multiplo de 3
# 3) somar os números que atende a condicional
# 4) apresentar os resultados

multiplo_tres = 0 # variavel que irá receber os números ímpares e multiplos de 3

for i in range(1,31,2): #contagem dos números ímpares
    if i % 3 == 0: #checagem se os números são múltiplos
        print(i, end=",") # apresentação dos números que atendem os 
        #requisitos (na mesma linha, separados por vírgula)    
        multiplo_tres += i
print() # pular uma linha
print(f"A soma dos números ímpares multiplos de 3 neste intervalo é {multiplo_tres}")

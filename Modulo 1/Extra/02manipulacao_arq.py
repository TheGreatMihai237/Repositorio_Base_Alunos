#Ler um arquivo

arquivo = open("pessoa.txt", "r") # a leitura é feita dentro do proprio sistema
conteudo = arquivo.read() # eu armazeno a leitura em uma variavel
print(conteudo) # peço para imprimir a leitura 
arquivo.close() # sempre que utiliazamos a função open() precisamos finalizar
# fechando o arquivo
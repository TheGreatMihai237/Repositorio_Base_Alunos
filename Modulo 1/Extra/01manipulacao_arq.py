# Criar arquivo, recebendo informação do usuário

# Solicitação de entrada
nome = input("Digite seu nome completo: ")
email = input("Digite seu email: ")

# Criar arquivo
arquivo = open("pessoa.txt","a",encoding="utf-8")# estamos criando o arquivo e 
# armazenando na variavel arqivo, o modo "a" escreve sempre no final,
# enconding utf-8 é para utilizar o conjunto de caracteres que engloba
# a lingua portuguesa
arquivo.write(nome + "|" + email + "\n") #.write é para escrever e o 
# \n é para pular linha
arquivo.close() # .close é para fechar o arquivo
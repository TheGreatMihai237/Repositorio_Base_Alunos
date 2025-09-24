try: # o codigo tenta executar o comando
    resultado = 10/0
except: # caso não consiga, ele apresenta qual é o erro
    print("Ocorreu um erro na operação. Não é possivel a divisão com o denominador igual a zero.")

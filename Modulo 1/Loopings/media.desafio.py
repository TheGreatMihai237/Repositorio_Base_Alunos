# Solicite ao usuario 4 notas.
# calcule a media
# informe se o aluno está aprovado (media>=7),recuperação(5<media<7) ou reprovado.
# apresente as notas que o aluno tirou, a media e o status de sua situação

# use, lista, for, if/elif/else


notas = []
for i in range(4):
    nota = float(input(f"informe a nota da prova {i+1}: "))
    if nota > 0: # só aceita nota positivas
        notas.append(nota) #notas.append adiciona um elemento no final da lista
    else: # se a nota for negativa apresenta o print
        print("valor inválido.")
print(f"suas notas são: {notas} ")
media = sum(notas)/len(notas)# a função sum(notas) soma todas as notas da lista
# a função len(notas) informa o tamanho da lista nostas

if media >=7: # se a media for maior que 7
    print(f"suas notas foram{notas}, sua {media:.2f} e você está aprovado. ")
elif 5 <= media <=7: # se a media for de 5 a 6.99
    print(f"suas notas foram{notas}, sua {media:.2f} e você está de recuperação. ")
else: # notas abaixo de 5, ou seja, de 4;99 até 0
    print(f"suas notas foram{notas}, sua {media:.2f} e você está reprovado. ")
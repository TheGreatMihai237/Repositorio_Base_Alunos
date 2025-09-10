# Crie um código que receba 3 notas, calcule a média
# e informe se o aluno está aprovado, em recuperação
# ou reprovado

# obs: aprovado media >= 7
# recuperação média > 4
# reprovado média < 4
# o mesmo que => elif media >= 5 and media < 7
# etapas

# 1) solicitar as notas ao usuario
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# 2)calcular a média
media = (n1 + n2 + n3)/3

# 3) checar a condição do aluno
if media >=7:
    print(f"O aluno de média {media:.2f} está aprovado")
elif 5 <= media <7: # o mesmo que => elif media >= 5 and media < 7
    print(f"O aluno de média {media:.2f} e está de recuperação")
else:
    print(f"O aluno teve média {media:.2f} e está reprovado")

# 4) Informar o resultado 
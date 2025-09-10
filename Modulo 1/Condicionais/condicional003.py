#criar um codigo python que indique se a temperatura está agradavel ou não
# condições:
# temperatura>=30° informar que está muito quente
# temperatira >=20° informar que a temperatura está agradavel
# temperatura >=10° informar que está muito frio
# temperatura abaixo de 10 informar que está muito frio

#Etapas para resolução:
# 1) Solicitar a temperatura para o usuario
# 2) verificar a condicional
# 3) imprimir a resposta segundo a temperatura

temperatura = float(input("Digite a temperatura do dia: "))

#


if temperatura >= 30:
    print(f"hoje a temperatura é {temperatura} graus e está muito quente")

elif temperatura >= 20:
    print(f"hoje a temperatura é {temperatura} está agradavel")

elif temperatura >= 10:
    print(f"hoje está {temperatura} graus e está frio")
else:
    print(f"hoje a temperatura é {temperatura} e está congelando")
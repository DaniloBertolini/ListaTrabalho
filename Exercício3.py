print("Conversão de Dias, Horas e Minutos para segundos!")

dias = int(input("Insira os dias: "))
horas = int(input("Insira as horas: "))
minutos = int(input("Insira os minutos: "))
segundos = int(input("Insira os segundos: "))

minutosC = minutos * 60
horasC = horas * 60 * 60
diasC = dias * 24 * 60 * 60

print("O total de segundos são", minutosC + horasC + diasC + segundos ,"segundos.")
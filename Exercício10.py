import math

lata = 80
galao = 25

metrospintar = int(input("Qual o tamanho da área para ser pintada:"))

litros_usar = (metrospintar / 6)

#A
latasnecessarias = math.ceil(litros_usar / 18)
print("Para a questão A, será necessário ",latasnecessarias,"lata(s).")
print("E pagará R$",latasnecessarias * lata)

#B
galoesnecessarios = math.ceil(litros_usar / 3.6)
print("Para a questão B, será necessário ",galoesnecessarios,"galões.")
print("E pagará R$",galoesnecessarios * galao)

#C
latasnecessarias = int(litros_usar / 18)
faltou = litros_usar % 18
galoesnecessarios =math.ceil(faltou / 3.6)

print("Para a questão C, será necessário",latasnecessarias,"lata(s) e",galoesnecessarios,"galões.")
print("E pagará R$",(latasnecessarias * lata) + (galoesnecessarios * galao))
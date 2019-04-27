mercadoria = int(input("Indique o preço da mercadoria: "))
desconto = int(input("Indique o percentual do desconto: "))

mercadorianova = mercadoria * desconto / 100
descontonovo = mercadoria - mercadorianova

print("O desconto da mercadoria é:" ,mercadorianova)
print("O novo preço a pagar é:" ,descontonovo)
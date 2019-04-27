kmpercorridos = int(input("Quantos Km foram percorridos com o carro alugado? R:"))
dias = int(input("Quantos dias este carro esta alugado? R:"))

preçocarro = 60 * dias
preçokm = 0.15 * kmpercorridos

print("O preço a pagar pelo carro é R$",preçocarro + preçokm)
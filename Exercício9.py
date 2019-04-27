cigarrosdia = int(input("Digite a quantidade de cigarros fumados por dia:"))
anosfumados = int(input("Digite quantos anos você fuma:"))

tempodia = cigarrosdia * 10
tempoano = ((anosfumados * 365) * tempodia) / (24 * 60)

print("Você perdeu {0:3.1f}".format (tempoano),"dias de vida")
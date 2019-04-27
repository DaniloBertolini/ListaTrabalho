salario = int(input("Digite seu salario atual: "))
aumento = int(input("Digite a porcentagem do aumento: "))

aumentosalario = salario * aumento / 100
salarionovo = salario + aumentosalario

print("O aumento do salário é:", aumentosalario)
print("Seu novo salário é:", salarionovo)
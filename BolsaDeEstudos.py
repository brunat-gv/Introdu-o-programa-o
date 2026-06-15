#Questão 1) Bolsa de Estudos.

ome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
mf = float(input("Informe sua média final: "))
rf = float(input("Informe a renda familiar mensal: "))

if idade < 16:
    print("Candidato não elegível: idade mínima não atingida.")

elif mf >= 9.0 and rf <= 2000:
    print("Bolsa Integral")
elif mf >= 8.0 and rf <= 3500:
    print("Bolsa de 50%")
elif mf >= 7.0 and rf <= 5000:
    print("Bolsa de 25%")
else:
    print("Não aprovado para bolsa")
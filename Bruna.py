#Questão 1) Bolsa de Estudos.

"""nome = str(input("Informe seu nome: "))
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


    
#Questão 2) Desconto.

v_c = float(input("Informe o valor da compra: "))
desconto20 = 0.20 * v_c
desconto10 = 0.10 * v_c
desconto5 = 0.05 * v_c

if v_c >= 500:
    print("desconto = ", desconto20, "Valor final: ", v_c - desconto20)
elif v_c  >= 200:
    print("desconto = ", desconto10, "Valor final =", v_c - desconto10)
elif v_c >= 100:
    print("desconto = ", desconto5, "Valor final =", v_c - desconto5)
else:
    print("desconto = ",0 )"""




#Questão 3) Classificação do compeonato.

invalida = 0
infantil = 0
juvenil = 0
junior = 0
adulto = 0

for i in range (10):
 
 nome = str(input("Informe seu nome: "))
 idade = int(input("Informe sua idade: "))

 if idade < 0:
    categoria = "invalida"
    invalida += 1
 elif idade >= 0 and idade < 12:
    categoria = "infantil"
    infantil += 1
 elif idade >= 12 and idade <= 14:
   categoria = "juvenil"
   juvenil += 1
 elif idade >= 15 and idade <=17:
   categoria = "junior"
   junior += 1
 else:
   categoria = "adulto"
   adulto += 1
print("Número total por categoria:")
print("Idade inválida", invalida)
print("Infantil", infantil)
print("Juvenil", juvenil)
print("Júnior", junior)
print("Adulto", adulto)


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
    print("desconto = ",0 )
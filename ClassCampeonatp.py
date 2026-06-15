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
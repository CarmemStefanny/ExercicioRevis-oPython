pergunta1 = input("Telefonou para a vítima ? ")
pergunta2 = input("Esteve no local ? ")
pergunta3 = input("Mora perto da vítima ? ")
pergunta4 = input("Devia para a vítima ? ")
pergunta5 = input("Já trabalhou com a vítima ? ")

cont = 0
if pergunta1 == "sim":
    cont += 1
if pergunta2 == "sim":
    cont += 1
if pergunta3 == "sim":
    cont += 1
if pergunta4 == "sim":
    cont += 1
if pergunta5 == "sim":
    cont += 1

if cont == 2:
    print("Suspeita")
elif cont == 3 or cont == 4:
    print("Cúmplice")
elif cont == 5:
    print("Assassino")
else:
    print("Inocente")

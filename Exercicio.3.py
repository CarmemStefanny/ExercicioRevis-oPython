pergunta1 = input("Telefonou para a v�tima ? ")
pergunta2 = input("Esteve no local ? ")
pergunta3 = input("Mora perto da v�tima ? ")
pergunta4 = input("Devia para a v�tima ? ")
pergunta5 = input("J� trabalhou com a v�tima ? ")

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
    print("C�mplice")
elif cont == 5:
    print("Assassino")
else:
    print("Inocente")

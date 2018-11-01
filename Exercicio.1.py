Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())
Media = Nota1+Nota2+Nota3
MediaFinal = Media / 3
if MediaFinal < 7:
    print("Reprovado")
if MediaFinal == 10:
    print("Aprovado com Distinção")
elif MediaFinal >= 7:
    print("Aprovado")

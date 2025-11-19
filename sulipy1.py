"""
1. Feladat
Írj egy programot, ami a felhasználótól három egész számot számot kér be egyesével, ezeket eltárolja egy listában, majd a képernyőre kiírja a lista tartalmát! Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet, és ismétlődjön meg a bekérés!
"""

while True:
    try:
        list = []
        a = int(input("Add meg az első számot: "))
        b = int(input("Add meg a második számot: "))
        c = int(input("Add meg a harmadik számot: "))

        list.append(a)
        list.append(b)
        list.append(c)

        print(list)
        break
    except ValueError:
        print("Nem számot adtál meg")
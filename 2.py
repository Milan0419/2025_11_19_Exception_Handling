osztando = 10
while True:
    try:
        oszto = int(input(f"Mennyivel osszam el az {osztando}-es szamot? "))
        print(f"A két szám osztásának eredménye: {osztando/oszto}")
        n = input("Akarod futtatni tovább (i/n): ")
        if n == "n":
            break
        elif n == "i":
            continue
        else:
            print("Ismeretlen attribútum")
    except ZeroDivisionError as e:
        print(e)
        print("ZeroDivisionError: Nullával nem lehet osztani!")
    except ValueError as e:
        print(e)
        print("ValueError: Nem számot adtál meg!")
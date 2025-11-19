while True:
    try:
        szam = int(input("Adj meg egy egész számot!:"))
        print(f"A szám négyzete: {szam ** 2}")
        n = input("Akarod futtatni tovább (i/n): ")
        if n == "n":
            break
    except ValueError:
        print("Nem számot adtál meg!")
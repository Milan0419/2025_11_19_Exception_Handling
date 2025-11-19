lista = []

for i in range(6):
    while True:
        try:
            szam = int(input(f"{i+1}. szám:"))
            lista.append(szam)
            break
    except ValueError:
        print(f"ValueError: Kérlek egész számot adj meg")
        
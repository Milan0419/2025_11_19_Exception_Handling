szamok = []
while len(szamok) < 3:
    try:
        szam = int(input("Adj meg 3 egész számot "))
        szamok.append(szam)
    except ValueError:
        print("Valueerror, kérlek egész számot adj meg ")
        
print(szamok)
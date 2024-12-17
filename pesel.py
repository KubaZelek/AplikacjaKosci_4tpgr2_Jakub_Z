def wprowadz_pesel(pesel):
    peselek = [int(digit) for digit in pesel]
    return peselek
def suma_kontrolna(pesel):
    waga = [1,3,7,9,1,3,7,9,1,3]
    S = 0
    R = 0       
    for i in range(len(pesel)-1):
        S +=  pesel[i]*waga[i]  
    M = S%10
    if M != 0:
        R = 10-M
    if R == pesel[10]:
        return True
    
    return False
    
def plec(pesel):
    if pesel[9] % 2 == 0:
        return 'K'
    else:
        return 'M'
inpucik = input("Wprowadz pesel: ")
pesel = wprowadz_pesel(inpucik)
czy_prawidlowy = suma_kontrolna(pesel)
jaka_plec = plec(pesel)
if czy_prawidlowy:
    print("Pesel jest zgodny")
else:
    print("Pesel jest niezgodny")
if jaka_plec == 'K':
    print("Plec: Kobieta")
else: 
    print("Plec: Mezczyzna")
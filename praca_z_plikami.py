from prettytable import PrettyTable as pt
import time

# # plik = open("dane\\moje_dane.txt", "rt")
# plik = open( r"dane\moje_dane.txt", "rt") # alternatywa - albo dodajemy R i wtedy jeden \, albo dwa \\
# zaw = plik.read()
# plik.close() # tutaj zamykamy plik po wczytaniu

# # alternatywa - tutaj plik automatycznie sie zamknie jak wyjdziemy z poziomu with
# with open(r"dane\moje_dane.txt", "rt") as plik:
#     zaw = plik.read()

# print(zaw)

# with open(r"dane\moje_dane.txt", "a") as plik:
#     plik.write("\nabcx")


# IMPORTUJEMY SAMOCHODY Z PLIKU DANE.CSV
MAX_WIERSZY = -1
ile = 0
suma_total = 0
ile_total = 0
pojazdy = {}

czas_start=time.time()


with open(r"dane\dane_2_mln.csv", "rt", encoding="utf-8") as plik:
    for wiersz in plik:
        if ile == 0:
            ile += 1
            continue
        else:
            # print(wiersz.strip()) # strip usuwa niewidzialne znaki (spacje, \n na koncu)
            ile += 1
            if ile == MAX_WIERSZY:
                break
            # właściwe działania
            lista = wiersz.split(";")
            # print(lista)
            pojazd = lista[1]
            cena = float(lista[2])
            suma_total += cena
            ile_total += 1
            # print(f"Pojazdow jest: {ile_total}, cena: {suma_total}") # tuataj by nam pisalo co linie odswiezaloby 1,2,3 ...

            # uzupelnianie slownika pomocniczego

            if pojazd not in pojazdy:
                pojazdy[pojazd] = [0, 0]

            cena_obl = pojazdy[pojazd][0] + cena
            liczba_obl = pojazdy[pojazd][1] + 1

            pojazdy[pojazd] = [cena_obl, liczba_obl]


print(f"Pojazdow jest: {ile_total}, cena: {suma_total}")  # a tutaj poszlo
# print(pojazdy)

tab = pt(["Pojazd", "Cena", "Ilość", "Średnia cena"])

for pojazd, x in pojazdy.items():
    cena = f"{x[0]:,.0f}".replace(","," ")
    ile = x[1]
    avg = round(x[0]/x[1],1)
    tab.add_row([pojazd, cena, ile, avg])
print(tab)

with open(r"dane\moje_dane.txt", "w", encoding="utf-8", newline="") as plik:
    plik.write(tab.get_string())
    plik.write("\n\n")
    plik.write(tab.get_csv_string(delimiter=";"))

czas_koniec = time.time()

ile_trwalo=czas_koniec-czas_start
print(f"Czas wykonania: {ile_trwalo:.2f} s")



from tkinter import simpledialog
from prettytable import PrettyTable as pt
from dane.dane_zdarzenia import zdarzenia

# print(zdarzenia)
format = simpledialog.askstring("format", "Wybierz format do zapisu: csv lub json")

if format == "None":
    print("Nie wybrales to nie masz :)")
    exit()

format = format.strip().lower()  # gdyby wpisal CSV csV jSoN itd

if format != "csv" and format != "json":
    print("zly format.")
    exit()

ile_serious = 0
ile_minor = 0
lotniska = {}
typy = {}


for data, lotnisko, typ, powaga, samolot in zdarzenia:
    # print(zdarzenie)
    if powaga == "minor":
        ile_minor += 1
    else:
        ile_serious += 1

    if lotnisko not in lotniska:
        lotniska[lotnisko] = [0, 0]

    lotniska[lotnisko][0] += 1
    if powaga == "serious":
        lotniska[lotnisko][1] += 1

    if typ not in typy:
        typy[typ] = 0
    typy[typ] += 1


ile_razem = ile_minor + ile_serious

print(f"Razem: {ile_razem}, minor: {ile_minor}, serious: {ile_serious}")

tab_lotniska = pt(["Lotnisko", "Liczba zdarzen", "Minor", "Serious", "Ryzyko (%)"])

lotniska_do_json={}


for lotnisko, dane in lotniska.items():
    razem=dane[0]
    serious=dane[1]
    minor=razem-serious
    ryzyko=round((serious/razem)*100,1)

    tab_lotniska.add_row([lotnisko, razem, minor, serious, f"{ryzyko}%"])
print(tab_lotniska)

tab_typy=pt( ["Typ zdarzenia", "Liczba"])

for typ, liczba in typy.items():
    tab_typy.add_row([typ, liczba])

print(tab_typy)


# zapis do pliku
if format=="csv":
    with open("dane\\dane.csv", "w", encoding="utf-8", newline="") as plik:
        plik.write(tab_lotniska.get_csv_string(delimiter=";"))
        plik.write("\n\n")
        plik.write(tab_typy.get_csv_string(delimiter=";"))
    print(f"\nZapisano do csv")

else:
    with open("dane\\dane.json", "w", encoding="utf-8") as plik:
            plik.write(tab_lotniska.get_json_string())
            plik.write(tab_typy.get_json_string())
    print(f"\nZapisano do JSON")
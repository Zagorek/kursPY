print("Cześć. Dzialamy")
import cowsay

"""
abc
abc
"""
# cowsay.cow("Cześć")
# cowsay.milk("Cześć")
# print( cowsay.char_names)
# CTRL /

print("tekst", "inny tekst")
print("tekst" + "inny tekst")  # konkatenacja tekstów &
print("=" * 60)  # mozna sobie oddzielic graficznie część

# zmienne
x = 5
y = 10
print(x + y)
z = x + y
print(z)
# Deklaracja
# Definicja zmiennej
abc = None

wartość = 1
print(wartość)

x, y, z = 1, "miesiac", 30  # mozna definiowac kilka zmiennych po przecinku

x = "Ala ma kota"  # str
y = 12  # int
z = 12.43  # float
q = 0.3  # 30%
w = True  # bool

y = "10.44"
xx = float(y) + z
xx = round(xx, 2)
print(xx)


wakacje = "Łeba"
kiedy = 15
kasa = 12363464.23452234
print("Na wakacje pojadę", kiedy, "do miasta", wakacje)
# alternatywa - F (od sformatowany) - string
print(f"Na wakacje pojadę {kiedy} do miasta {wakacje} wydam {kasa:,.2f}")

# a jak chcemy ladna liczbe ale w zapisie polskim
ładna_liczba = f"{kasa:_.2f}".replace(
    "_", " "
)  # najpierw przedstawilismy liczbe jako XXX_XXX_XXX.YY a potem zamienilismy _ na spacje
print(f"Liczba: {ładna_liczba}")
a = 2
b = 3
print(a**b)  # potegowanie to dwie gwiazdki

print(len(ładna_liczba)) # liczba znakow liczby '12 363 464.23'
print(type(ładna_liczba)) # sprawdza jaki jest typ zmiennej

print("Na wakacje pojadę", kiedy, "do miasta", wakacje, sep="-") # teraz domyslnym separatorem jest '-' a nie spacja ( tam gdzie byla spacja teraz jest myslnik)

b="Hello, World!"
print(b[2:5]) # Wycina znaki od 2 do 4, przedzial: [2, 5)
# print([::,-1])

imie="mateusz"
poprawione_imie=imie.upper()
print(poprawione_imie)
print("=" * 60)
imie.title() #ta funkcja dostarcza wynik, ale nie modyfikuje zmiennej - teskty sa niezmienne!
print(imie)

#lepiej:
print(imie.title())

#albo nadpisac zmienna:
imie=imie.title()
print(imie)

#lancuch wywolan:
imie=imie.title().replace("z","ź") # tak czesto robi AI, wiec na poczatku przygody z AI mozna napisac nie korzystaj z lancucha wywolan i moze byc bardziej po ludzku
print(imie)

#lamanie tekstu - dodanie \ na koncu + enter:
imie=imie.title().replace("z","ź").replace("a","t"). \
    replace("ź","z")
print(imie)


print("=" * 60)
print("Ćwiczenie #1")
print("=" * 60)
from datetime import datetime, date, timedelta
import relativedate

tekst_CSV= "03/22/2025 jan KOWalski wypłata PLN: 8359"

# Rozdzielanie daty z biblioteka datetime
data=tekst_CSV[0:10]
data_prawidłowa=datetime.strptime(data, "%m/%d/%Y")
print(data_prawidłowa.date())

# Rozdzie 
print(f"Data RRRR, MM, DD: {tekst_CSV[6:10]}, {tekst_CSV[0:2]}, {tekst_CSV[3:5]}")

imie_nazwisko=tekst_CSV[11:tekst_CSV.find(" wypłata")].title()
print("Imie i nazwisko: ",imie_nazwisko)

wypłata=tekst_CSV[tekst_CSV.find(": ")+1:] # tekst
wypłata_w_euro=float(tekst_CSV[tekst_CSV.find(": ")+1:])/4.33
print(f"Wypłata w Euro: {wypłata_w_euro:,.2f}".replace(',',' ').replace('.',','))

# albo
print(f"{tekst_CSV[6:10]}-{tekst_CSV[0:2]}-{tekst_CSV[3:5]} {imie_nazwisko} {wypłata_w_euro:.2f}")




teraz=datetime.now()
print(f"Teraz jest: {teraz}")

urodziny=date(1995, 10, 25)
print(f"Urodziny: {urodziny}")

przyszlosc=urodziny+timedelta(days=100)
print(przyszlosc)

ladna_data=teraz.strftime("%d.%m.%Y %H:%M:%S")
print(f"Format europejski: {ladna_data}")
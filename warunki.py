# bloki warunkowe - warunek, dwukropek, wcięcie

kolor = "zielony"

if kolor == "biały":
    print("kupię")
elif kolor == "różowy":
    print("SUPER!")
# opcjonalnie
else:
    print("nie kupię")
print("test")

kolor = "zielony"
cena = 90000

#############################################################
# kupie w cenie do 65k zielony
print("=" * 60)

if (kolor == "zielony" or kolor == "biały") and cena <= 65000:  # pamietac o nawiasach
    print("kupie")
else:
    print("nie kupie")

#############################################################
# pobranie od usera
print("=" * 60)

# test="42sgs"
# a = test.isdigit()
# print(a)


# cena = input("Podaj cenę: ")
# if cena == "":
#     print("brak ceny")
# elif cena.isdigit() == False:
#     print("niepoprawna liczba!")
# # elif not cena.isdigit():
# #     print("niepoprawna liczba!")
# else:
#     print(f"cena: {cena}")

from tkinter import simpledialog

tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
kurs = simpledialog.askfloat(
    "Kurs", "Podaj kurs Euro", minvalue=1, maxvalue=10, initialvalue=4.5
)

if kurs == None:
    print("Nie podales kursu")
else:
    wypłata_w_euro = float(tekst_CSV[tekst_CSV.find(": ") + 1 :]) / kurs
    print(f"Wypłata w Euro: {wypłata_w_euro:,.2f}".replace(",", " ").replace(".", ","))

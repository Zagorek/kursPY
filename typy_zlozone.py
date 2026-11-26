# listy

owoce = ["jabłko", "banan", "wiśnia", "banan"]
print(owoce[1])
print(owoce[1:3])


owoce[1] = "truskawka"  # zamienienie drugiego elementu truskawką
owoce.append("cytryna")  # dodanie do elementu do listy na koncu
print(owoce)


owoce.sort()  # listy sa zmienialne w przeciwienstwie do stringów (patrz plik start.py) - dlatego funkcje ktore uruchamiamy do niczego nie przypisujemy: nie piszemy X=X.sort() tylko od razu X.sort()

owoce.append(["x", "y"])  # dodaje liste zagniezdzona do listy owoce
owoce.extend(
    ["x", "y"]
)  # rozpakowuje elementy i dodaje je osobno do listy jako elementy a nie jako liste
print(owoce)

owoce = [
    ["jabłko", "banan", "wiśnia", "banan"],
    ["jabłko", "banan", "wiśnia", "baxxxnan", "abc"],
]
el = owoce[1][3]  # owoce[wiersz][kolumna]
print(el)
print(owoce[1])
print("=" * 60)
print(len(owoce[1]))

tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
moja_lista = tekst_CSV.split(" ")
print(moja_lista)
# ['03/22/2025', 'jan', 'KOWalski', 'wypłata', 'PLN:', '8359']

moja_lista.append(moja_lista[1] + " " + moja_lista[2])
moja_lista.pop(1)
moja_lista.pop(1)
# alternatywa
# del moja_lista[2:4]
print(moja_lista)

# skorygowanie znakow imienia i nazwiska
moja_lista[4] = moja_lista[4].title()
print(moja_lista)
print("=" * 60)

#############################################################
# krotki - tuple

owoce = ("jabłko", "banan", "wiśnia", "banan")  # to jest krotka
# owoce[0]="zosia" nie zadziala, bo krotki sa niezmienialne


punkt = (10, 20)
x, y = punkt
print(x)
# 10
print(y)
# 20

print(10 in punkt)  # Wynik: True (bo 10 jest w krotce o nazwie punkt)



#############################################################
# Zestawy, zbiory (sets)
print("=" * 60)

owoce = {"jabłko", "banan", "wiśnia", "banan"} # tworzy set (zbior) czyli usuwa duplikaty, ale elementy oddaje w sposob nieuporzadkowany, losowy
print(owoce)

owoce = ["jabłko", "banan", "wiśnia", "banan"]
unikalne = list( set(owoce) ) # to tworzy z listy set a potem znowu liste, czyli liste bez duplikatow
print(unikalne)

#############################################################
# Słowniki (dictionaries)
print("=" * 60)

# klucz w slowniku musi byc niezmienialny (string, liczba, krotka)
dict= {
    "brand": "Ford",
    "model": "Mondeo",
    "year": 2018,
    10: "abc", # zrozumiec dlaczego liczba jest niezmienialna
    (1,5): "xyz",
    "wlasciwosci": ["skora", "klima"]
}
print(dict)

x=dict["model"]
print(x)

y=dict.get("model")
print(y)

# z=dict["model_auta"] to by nie zadzialalo bo nie ma takiego klucza
z=dict.get("model_auta", "brak danych") #nie znalazlo, ale nie wywalilo bledu bo dalem jak nie znajdziesz to napisz brak danych
print(z)

print(dict["wlasciwosci"][1]) # odczytuje drugi element klucza (tj. listy) wlasciwosci 
print("=" * 60)


dict["year"]=2023 # jesli istnieje juz taki klucz to sie nadpisze
dict["kolor"]="czarny" # jesli nie istnieje to sie doda

print(dict)

print("=" * 60)

print(dict.items())
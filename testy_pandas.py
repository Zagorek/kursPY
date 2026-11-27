import pandas as pd

# odzcyt pliku
df = pd.read_excel(r'dane\samochody.xlsx', sheet_name="dane") # z excela

# print(df.head(10)) - wyswietla 10 pierwszych wierszow (zeby spojrzec jaka jest struktura pliku)
# print(df.shape) - wyswietla rozmiar pliku (wiersze x kolumny)

# df2=pd.read_csv(r'dane\dane_2_mln.csv', sep=";", encoding="utf-8-sig") # z csv
# print(df2.shape)

print(df.columns.tolist()) # wypisanie kolumn

print(df.dtypes) # sprawdzenie jakiego typu sa zmienne

# nazwy=df["Marka"].unique()
# print(nazwy)

# drogie_pojazdy = df[df["Cena_PLN"]>50000]
# print(drogie_pojazdy)

# Podmienienie by wszystkie marki byly z malej litery
marka=df["Marka"].astype("string")
marka=marka.str.lower()
df["Marka"]=marka


# wiersze spelniajace warunek i wybrane kolumny
kolumny = ['Kolor', 'Cena_PLN', 'Marka']
filtr = ((df["Kolor"] == "Czerwony") | (df["Kolor"] == "Biały")) & (df["Cena_PLN"] <= 80000) & (df["Marka"].str.contains("bmw", case=False))

#filtr = df["Kolor"].isin(["Czerwony", "Biały"]) & (df["Cena_PLN"] <= 50000)

# df_filtr = df.loc[filtr , kolumny]

wynik = (df.loc[filtr].sort_values(["Kolor", "Cena_PLN"], ascending=[True, False]))

print(wynik)

# szukanie brakujacych wartosci
wynik = df[df.isna().any(axis=1)] # szukanie na poziomie wiersza (axis=1), axis=0 byloby dla poziomu kolumn
print(wynik)

df['Cena_brutto'] = df["Cena_PLN"] * 1.23
print(df)

df["Marka_model"]=(df["Marka"].astype("string")+" "+ df["Model"])
print(df)

df.loc[df["Kolor"].isin(["Czerwony", "Biały"]), "Kategoria_pieknosci"] = "Ładny"

df.loc[~df["Kolor"].isin(["Czerwony", "Biały"]), "Kategoria_pieknosci"] = "Brzydki"

print(df[["Kolor", "Kategoria_pieknosci"]])

# liczba niepustych cen
liczba=df["Cena_PLN"].count()

print(liczba)

# Suma cen wszystkich ofert
suma=df["Cena_PLN"].sum()
print(suma)

# Sprawdzenie ile jest samochodow danej marki, resetindex nadaje nazwe kolumnie ktora sie stworzyla
liczba_ofert=df.groupby("Marka").size().sort_values(ascending=False).reset_index(name="Liczba_ofert")
# print(liczba_ofert)



lokalizacje = df["Lokalizacja"].unique()
print(lokalizacje)

for lok in lokalizacje:

    ramka_filtr=df.loc[ df["Lokalizacja"] == lok]

    statystyki_marek=(
        ramka_filtr.groupby("Marka", as_index=False)
        .agg(
            Liczba_ofert=("Cena_PLN", "count"),
            Suma_cen=("Cena_PLN", "sum"),
            Sredni_przebieg=("Przebieg_KM", "mean")
        ).sort_values("Liczba_ofert", ascending=False)
    )
    # print(statystyki_marek)



    moja_ramka=pd.DataFrame([{
        "Marka": "TOTAL",
        "Liczba_ofert": statystyki_marek["Liczba_ofert"].sum(),
        "Suma_cen": statystyki_marek["Suma_cen"].sum(),
        "Sredni_przebieg": statystyki_marek["Sredni_przebieg"].mean()
    }])
    # print(moja_ramka)

    statystyki_marek=pd.concat([statystyki_marek, moja_ramka])

    # print(statystyki_marek)

    statystyki_marek.to_excel("dane\\" + lok + ".xlsx", index=False, sheet_name="moje_dane")


# policz ile jest pojazdow ladnych i brzydkich

print(df)
pieknych=0
brzydkich=0
total=df["Kategoria_pieknosci"].count()

kolorki = df["Kategoria_pieknosci"]
for kolor in kolorki:
    if kolor == "Ładny":
        pieknych+=1
    else:
        brzydkich+=1

print(f"Ładnych: {pieknych} ({pieknych/total*100:.2f}%), Brzydkich: {brzydkich} ({brzydkich/total*100:.2f}%)")
# bloki warunkowe - warunek, dwukropek, wcięcie

kolor="zielony"

if kolor == "biały":
    print("kupię")
elif kolor == "różowy":
    print("SUPER!")
#opcjonalnie
else:
    print("nie kupię")
print("test")

kolor = "zielony"
cena = 90000

#############################################################
#kupie w cenie do 65k zielony
print("=" * 60)

if (kolor == "zielony" or kolor == "biały") and cena<=65000: # pamietac o nawiasach
    print("kupie")
else:
    print("nie kupie")
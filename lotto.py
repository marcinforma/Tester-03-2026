import random

print("podaj 6 różnych liczb w zakresie 1-49 oddzielone przecinkiem")
moje_liczby = (input())
moje_liczby_lista = [int(x) for x in moje_liczby.split(",")]
print(moje_liczby_lista)

pula_liczb = range(1, 50)
wylosowane_liczby = random.sample(pula_liczb, 6)
wylosowane_liczby.sort()
print("Wylosowane liczby to:", wylosowane_liczby)

trafione = list(set(moje_liczby_lista) & set(wylosowane_liczby))

print(f"Trafione liczby: {trafione}")
print(f"Liczba trafień: {len(trafione)}")
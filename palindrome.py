def czy_palindrom(wyraz):
    return wyraz.lower() == wyraz[::-1].lower()

tekst = input('Podaj słowo: ')

if czy_palindrom(tekst):
    print(f'Słowo "{tekst}" jest palindromem.')
else:
    print(f'Słowo "{tekst}" NIE jest palindromem.')

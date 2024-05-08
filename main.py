# Definiujemy klasę Osoba
class Osoba:
    def __init__(self, imie, nazwisko, wiek, miasto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.miasto = miasto

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, {self.wiek} lat, {self.miasto}"

    def __repr__(self):
        return self.nazwisko


# Definiujemy listę osób zgodnie z poleceniem
lista = [
    Osoba("Ola", "Kowalska", 5, "Gdynia"),
    Osoba("Ela", "Śmigalska", 34, "Lublin"),
    Osoba("Michał", "Kowalski", 23, "Gdynia"),
    Osoba("Paweł", "Tokarski", 31, "Poznań"),
    Osoba("Michał", "Makowski", 25, "Gdynia"),
    Osoba("Ela", "Tkaczyk", 28, "Poznań"),
    Osoba("Paweł", "Mirecki", 34, "Lublin"),
    Osoba("Paweł", "Dobrocki", 14, "Gdynia"),
    Osoba("Weronika", "Kowalewska", 19, "Toruń")
]

# 1.1. Lista osób z Gdyni
osoby_z_gdyni = list(filter(lambda osoba: osoba.miasto == "Gdynia", lista))
print('Lista osób z Gdyni:', osoby_z_gdyni)

# 1.2. Lista osób w wieku co najmniej 25 lat posortowana według nazwisk
osoby_25_lat_i_wiecej = filter(lambda osoba: osoba.wiek >= 25, lista)
osoby_25_lat_i_wiecej_posortowane = sorted(osoby_25_lat_i_wiecej, key=lambda osoba: osoba.nazwisko)
print('Lista osób w wieku co najmniej 25 lat posortowana według nazwisk:', osoby_25_lat_i_wiecej_posortowane)

# 1.3. Lista osób, których imię składa się z więcej niż 3 liter posortowana według wieku
osoby_imie_dluzsze_niz_3_litery = filter(lambda osoba: len(osoba.imie) > 3, lista)
osoby_imie_dluzsze_niz_3_litery_posortowane = sorted(osoby_imie_dluzsze_niz_3_litery, key=lambda osoba: osoba.wiek)
print('Lista osób, których imię składa się z więcej niż 3 liter posortowana według wieku:',
      osoby_imie_dluzsze_niz_3_litery_posortowane)

# 1.4. Średni wiek osób z Poznania
osoby_z_poznania = filter(lambda osoba: osoba.miasto == "Poznań", lista)
lista_osob_z_poznania = list(osoby_z_poznania)
liczba_osob_z_poznania = len(lista_osob_z_poznania)
suma_wiekow = sum(osoba.wiek for osoba in lista_osob_z_poznania)
sredni_wiek = suma_wiekow / liczba_osob_z_poznania if liczba_osob_z_poznania > 0 else 0
print('Średni wiek osób z Poznania:', sredni_wiek)

# 1.5. Liczba osób z każdego miasta
from collections import Counter

liczba_osob_z_kazdego_miasta = Counter(osoba.miasto for osoba in lista)
print('Liczba osób z każdego miasta:', liczba_osob_z_kazdego_miasta)

# 1.6. Liczby osób z tym samym imieniem
liczba_osob_z_tym_samym_imieniem = Counter(osoba.imie for osoba in lista)
print('Liczby osób z tym samym imieniem:', liczba_osob_z_tym_samym_imieniem)

# 1.7. Lista osób, których imię rozpoczyna się na E
osoby_z_imieniem_zaczynajacym_sie_na_E = filter(lambda osoba: osoba.imie.startswith('E'), lista)
print('Lista osób, których imię rozpoczyna się na E:', list(osoby_z_imieniem_zaczynajacym_sie_na_E))

# 1.8. Lista osób, których imię zawiera "la"
osoby_z_imieniem_zawierajacym_la = filter(lambda osoba: 'la' in osoba.imie, lista)
print('Lista osób, których imię zawiera "la":', list(osoby_z_imieniem_zawierajacym_la))

# 1.9. Lista wszystkich miast, bez powtórzeń, posortowana alfabetycznie
wszystkie_miasta = sorted(set(osoba.miasto for osoba in lista))
print('Lista wszystkich miast, bez powtórzeń, posortowana alfabetycznie:', wszystkie_miasta)

# 1.10. Wiek najstarszej osoby
najstarsza_osoba = max(lista, key=lambda osoba: osoba.wiek)
print('Wiek najstarszej osoby:', najstarsza_osoba.wiek)

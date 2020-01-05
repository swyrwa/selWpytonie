# zad1
# def suma():
#     liczba1 = input("Podaj liczbę numer 1: ")
#     liczba2 = input("POdaj liczbę numer 2: ")
#     return print("Suma dwóch podanych przez Ciebie liczb to: " + str(liczba1+liczba2))
#
# suma()

# zad2
# silnia iteracyjnie
# def silniaLiczby(liczba):
#     x = 1
#     silnia = 1
#     while x < liczba:
#         silnia = silnia * (x + 1)
#         x = x + 1
#     return silnia
#
# print(silniaLiczby(5))

# zad3
# silnia rekurencyjna
# def silniaRekurencyjna(liczba):
#     if liczba == 1:
#         wynik = liczba
#         print(wynik)
#         return wynik
#     else:
#         wynik = liczba * silniaRekurencyjna(liczba - 1)
#         print(wynik)
#         return wynik
#
#
# silniaRekurencyjna(4)

# zad4
# choinka
# def rysujChoinke(wysokosc):
#     x = 1
#     y = wysokosc
#     z = 1
#     while z <= wysokosc:
#         print((y-1)*' ' + x*'*' + (y-1)*' ')
#         y = y - 1
#         x = x + 2
#         z = z + 1
#
# rysujChoinke(4)

#zad5
# sprawdzanie czy liczba jest pierwsza
#
# def czyLiczbaPierwsza():
#     liczba = int(input("Podaj liczbę: "))
#     dzielniki = list()
#     for i in range(2, liczba-1):
#         if liczba % i == 0:
#             dzielniki.append(i)
#     if len(dzielniki) != 0:
#         print(dzielniki)
#         return print("{} to nie jest liczba pierwsza.".format(liczba))
#     else:
#         return print("{} jest liczbą pierwszą.".format(liczba))
# czyLiczbaPierwsza()
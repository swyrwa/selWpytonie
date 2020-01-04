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
# def silniaRekurencyjna(liczba)

# zad4
# choinka
def rysujChoinke(wysokosc):
    x = 1
    y = wysokosc
    while x <= wysokosc:
        print((y-1)*' ' + x*'*' + (y-1)*' ')
        y = y - x
        x = x + 1



rysujChoinke(8)
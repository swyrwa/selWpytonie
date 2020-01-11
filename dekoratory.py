def funkcjaZwyczajna(x):
    return x + 1


def funkcjaDoFunkcji(f, x):
    return f(x)


def funkcjaZewnetrzna(x):
    def funkcjaWewnetrzna(y):
        return x * y

    return funkcjaWewnetrzna


def funckjaDoFunckjiZewn(f):
    def funkcjaWewnetrzna(x):
        print("Tutaj funkcja wewnetrzna")
        wynik = f(x)
        return wynik + 1

    return funkcjaWewnetrzna


# print(funkcjaDoFunkcji(funkcjaZwyczajna,2))
# print(dir(3))

# f = funkcjaZewnetrzna(3)
# print(f(2))

# f = funckjaDoFunckjiZewn(funkcjaZwyczajna)
# print(f(2))


def dekoratorek(f):
    def funkcjaWewnetrzna(x):
        print("Tutaj funkcja wewnetrzna")
        wynik = f(x)
        return wynik + 1

    return funkcjaWewnetrzna


def funkcjaZwyczajna1(x):
    return x + 1


@dekoratorek
def funkcjaZwyczajna1(x):
    return x + 1
print(funkcjaZwyczajna1(2))
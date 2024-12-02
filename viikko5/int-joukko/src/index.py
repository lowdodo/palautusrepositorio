import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa_listalle(1)
    joukko.lisaa_listalle(2)
    joukko.lisaa_listalle(3)
    joukko.lisaa_listalle(2)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()

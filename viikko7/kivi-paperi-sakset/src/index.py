from sovellus import luo_uusi_peli
from tuomari import Tuomari

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        uusi_peli = luo_uusi_peli(vastaus)

        if uusi_peli:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            uusi_peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
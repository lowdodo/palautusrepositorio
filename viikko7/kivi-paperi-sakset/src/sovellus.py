from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_uusi_peli(input, tuomari):
    if input == "a":
        return KPSPelaajaVsPelaaja(tuomari)
    elif input == "b":
        return KPSTekoaly(tuomari)
    elif input == "c":
        return KPSParempiTekoaly(tuomari)
    else:
        return None
    
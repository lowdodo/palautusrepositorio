# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") # muutos mainissa
print(f"{x} - {y} = {erotus(y, y)}") # muutos mainissa


logger("lopetetaan ohjelma mainissa niin että tulisi virhe")
print("goodbye!")
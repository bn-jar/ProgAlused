
from datetime import date, datetime
import math


# 1

tana = date.today()

print(f"Tere! Täna on {tana}")

datetime.today()

# TODO


# 2

tehe = 3 + 8 / (4 - 2) * 4
print("Tehte vastus: " + tehe)

# Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# kui ei kasuta sulgusid, siis jagamine ja korrutamine toimuvad teisiti

# Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

print("Teise tehte vastus: " + 3 + 8 / 4 - 2 * 4) # jagamine on 8 / 4, mitte 8 / 2

print("Kolmanda tehte vastus: " + (3 + 8) / 4 - 2 * 4) # jagamine on 11 / 4, mitte 8 / 4


# 3

# ruut, mille sees on ring

R = 12 # ringi raadius on 12
S = math.pi * (R * R) # ringi pindala
C = 2 * math.pi * R # ringi ümbermõõt

# TODO


# 4

maa_raadius = 6378 # km

# TODO


# 5

for i in range(10):
    if i != 2 and i != 5:
        print("KILL")
    else:
        print("KILLADI")
    print("-KOLL")


# 6

laulusonad = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""

print(laulusonad.upper)

# 7

a = int(input("Sisesta ristküliku pikkus: "))

b = int(input("Sisesta ristküliku laius: "))

umbermoot = a * 2 + b * 2
pindala = a * b

print(f"Ristküliku ümbermõõt on {umbermoot} ja pindala on {pindala}")


# 8

tangitud_liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
labitud_km = float(input("Sisesta läbitud kilomeetrid: "))

# TODO


# 9

keskmine_kiirus = 29.9 # km/h
kiirus_minutites = keskmine_kiirus * 3.6

minutid = float(input("Mitu minutit rulluisutaja sõitis? "))

kaugus = kiirus_minutites * minutid / 3.6 # ?

print("Rulluisutaja jõuab " + minutid + " minutiga " + kaugus * " km kaugusele") # vale arvatavasti
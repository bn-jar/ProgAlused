# coding: iso-8859-1 -*-
import math
from calendar import monthrange
from datetime import date

# 1
# Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev moduli datetime kasutades ja date.today() funktsiooni abil.

tana = date.today()

print(f"Tere! Täna on {tana}")

print("Kuupäeva erinevad formaadid:")
print(tana.strftime("%d/%m/%Y"))
print(tana.strftime("%B %d, %Y"))
print(tana.strftime("%m/%d/%y"))
print(tana.strftime("%b-%d-%Y"))

print("Kuupäeva andmed:")
print(f"Päev: {tana.day}")
print(f"Kuu: {tana.month}")
print(f"Aasta: {tana.year}")

kuu_lopp = date(tana.year, tana.month, monthrange(tana.year, tana.month)[1])
paevi_kuu_lopuni = (kuu_lopp - tana).days

aasta_lopp = date(tana.year, 12, 31)
paevi_aasta_lopuni = (aasta_lopp - tana).days

print("Päevi kuu lõpuni:", paevi_kuu_lopuni)
print("Päevi aasta lõpuni:", paevi_aasta_lopuni)

sunnipaev = date(2006, 10, 9)

vanus_aastates = tana.year - sunnipaev.year
vanus_kuudes = tana.month - sunnipaev.month
vanus_paevades = tana.day - sunnipaev.day

if vanus_paevades < 0:
    vanus_kuudes -= 1
    eelmine_kuu = tana.month - 1 or 12
    eelmine_aasta = tana.year if tana.month > 1 else tana.year - 1
    vanus_paevades += monthrange(eelmine_aasta, eelmine_kuu)[1]

if vanus_kuudes < 0:
    vanus_aastates -= 1
    vanus_kuudes += 12

print(
    f"Minu vanus: {vanus_aastates} aastat, {vanus_kuudes} kuud ja {vanus_paevades} päeva."
)

# 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?

tehe = 3 + 8 / (4 - 2) * 4
print(f"Tehte vastus: {tehe}")

# Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# kui ei kasuta sulgusid, siis jagamine ja korrutamine toimuvad teisiti

# Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

print(f"Teise tehte vastus: {3 + 8 / 4 - 2 * 4}")  # jagamine on 8 / 4, mitte 8 / 2

print(
    f"Kolmanda tehte vastus: {(3 + 8) / 4 - 2 * 4}"
)  # jagamine on 11 / 4, mitte 8 / 4


# 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.

# ruut, mille sees on ring
R = 12  # ringi raadius

S_ring = math.pi * R**2
C_ring = 2 * math.pi * R

a = 2 * R  # ruudu külje pikkus (ringi diameeter)
S_ruut = a**2
C_ruut = 4 * a

print("Ruudu pindala:", S_ruut)
print("Ruudu ümbermõõt:", C_ruut)
print("Ringi pindala:", S_ring)
print("Ringi ümbermõõt:", C_ring)

# 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.

# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?

maa_raadius = 6378  # km
mundi_diameeter = 25.75  # mm

maa_umbermoot = 2 * math.pi * maa_raadius  # km

maa_umbermoot_mm = maa_umbermoot * 1000000

muntide_arv = maa_umbermoot_mm / mundi_diameeter

muntide_arv = math.ceil(muntide_arv)

print("Maa ümbermõõt:", round(maa_umbermoot, 2), "km")
print("2-eurose mündi läbimõõt:", mundi_diameeter, "mm")
print("Vajalike 2-euroste müntide arv:", muntide_arv)


# 5
# Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll
# kill-koll

# Saab kasutada muutujaid. Kuva iga sõna suure tähega.

for i in range(10):
    if i != 2 and i != 5:
        print("KILL", end="")
    else:
        print("KILLADI", end="")
    print("-KOLL", end=" ")


# 6
# Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:

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

print(laulusonad.upper())

# 7
# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.

a = int(input("Sisesta ristküliku pikkus: "))

b = int(input("Sisesta ristküliku laius: "))

umbermoot = a * 2 + b * 2
pindala = a * b

print(f"Ristküliku ümbermõõt on {umbermoot} ja pindala on {pindala}")


# 8
# Kütusekulu arvutamine
#     Kasutaja sisestab tangitud kütuse liitrid
#     Kasutaja sisestab läbitud kilomeetrid
#     Programm leiab kütusekulu 100km kohta keskmiselt

tangitud_liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
labitud_km = float(input("Sisesta läbitud kilomeetrid: "))

kulu_100km = (tangitud_liitrid / labitud_km) * 100

print(f"Keskmine kütusekulu: {kulu_100km} l/100 km")


# 9
# Rulluisutaja keskmine kiirus on 29,9km/h
# Kui kaugele jõuab M minutiga

keskmine_kiirus = 29.9  # km/h

minutid = float(input("Mitu minutit rulluisutaja sõitis? "))

aeg_tundides = minutid / 60
teepikkus = keskmine_kiirus * aeg_tundides

print(
    "Rulluisutaja jõuab "
    + str(minutid)
    + " minutiga "
    + str(teepikkus)
    + " km kaugusele"
)

# 10
# Kasutaja sisestab aja minutites
# Sinu valem leiab ja väljastab tunnid ja minutid
# Näiteks: sisestus 72, vastus 1:12

minutid = int(input("Sisesta aeg minutites: "))

tunnid = minutid // 60
jaak_minutid = minutid % 60

print(f"Aeg on {tunnid}:{jaak_minutid}")

# coding: iso-8859-1 -*-
import array
import math
from random import randint

print("Tere maailm!")


try: 
    # 1
    kasutaja_nimi = input("Mis on sinu nimi? ")

    print("Tere maailm! Tervitan sind " + kasutaja_nimi)

    vanus = input("Mis on sinu vanus? ")

    print(
            "Tere maailm! Tervitan sind "
            + kasutaja_nimi
            + "! Sa oled "
            + vanus
            + " aastat vana."
        )

    # 2
    # int
    vanus = 18
    print(type(vanus))

    # str
    eesnimi = "Jaak"
    print(type(eesnimi))

    # float
    pikkus = 16.5
    print(type(pikkus))

    # bool
    kas_kaib_koolis = True
    print(type(kas_kaib_koolis))


    # 3
    kommide_alg_arv = randint(1, 10)
    print("Laual on " + str(kommide_alg_arv) + " kommi")

    voetud_kommid = int(input("Mitu kommi sooviksid ära võtta? "))

    kommid = kommide_alg_arv - voetud_kommid

    print("Laual on nüüd " + str(kommid) + " kommi.")


    # 4
    C = float(input("Mis on puu ümbermoot? "))

    d = C / math.pi

    print("Puu läbimõõt on " + str(d))


    # 5
    N = float(input("Mis on ristküliku pikkus? "))
    M = float(input("Mis on ristküliku laius? "))

    d = math.sqrt(N * N + M * M)

    print("Ristkülikukujulise maatüki diagonaal on " + str(d))


    # 6
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))

    # v = s/t
    # kiirus = aeg / teepikkus

    kiirus = teepikkus / aeg

    print("Sinu kiirus oli " + str(kiirus) + " km/h")


    # 7
    suvalised_arvud = array.array('i', (randint(1, 10) for i in range(5)))

    summa = sum(suvalised_arvud)

    print("Arvude summa on " + str(summa))

    jagaja = int(input("Millega sooviksid seda jagada? "))

    if (jagaja > summa):
        print("Jagaja ei saa olla suurem kui summa!")
        exit()

    jagatud = abs(math.trunc(summa / jagaja))

    osa = abs(math.trunc(summa - (jagaja * jagatud)))

    print("Jagatud: " + str(jagatud) + ", osa: " + str(osa))

    # 8
    print("""
        @..@
       (----)
      ( \\__/ )
      ^^ "" ^^  
        """)

    # 9
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)

    print("Kolmnurga küljed on " + str(a) + ", " + str(b) + ", ja " + str(c))

    P = a + b + c

    print("Kolmnurga ümbermööt on " + str(P))

    # 10
    sobrad = randint(2, 5)

    pitsa_hind = 12.90

    # jootraha = 10 # %

    hind_kokku = pitsa_hind * 1.1

    makstud_inimese_kohta = hind_kokku / sobrad

    print(str(sobrad) + " sõpra ostsid koos pitsa, iga inimene pidi maksma " + str(makstud_inimese_kohta) + " eurot.")

except:
    print("Programmis tekkis viga!")
    exit()
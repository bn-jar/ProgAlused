
# coding: iso-8859-1 -*-
# ei luba teha "import * from math"
import math

print("Ruudu karakteristikud")

# peab tegema numbriks, et kalkulatsioonid (S=a**2) toimiksid
a = input("Sisesta ruudu külje pikkus => ")

if not a.isdigit():
  print("Sisesta number!")
  exit()

a = float(a)

S = a**2

print("Ruudu pindala", S)

P = 4 * a

# str lõpus peab olema closing quote (")
print("Ruudu ümbermõõt", P)

# kirjaviga, sqr -> sqrt
di = a * math.sqrt(2)

print("Ruudu diagonaal", round(di, 2))

print()

# ebakorrektne syntax, üleliigne sulg lõpus
print("Ristküliku karakteristikud")

# sama probleem mis ennem
b = input("Sisesta ristküliku 1. külje pikkus => ")
c = input("Sisesta ristküliku 2. külje pikkus => ")

if not b.isdigit() or not c.isdigit():
  print("Sisesta number!")
  exit()

b = float(b)
c = float(c)

# muutuja S on juba defineeritud
S2 = b * c

# syntax viga
print("Ristküliku pindala", S2)

# kordusmärk oli puudu, P on juba defineeritud
P2 = 2 * (b + c)

print("Ristküliku ümbermõõt", P2)
di = math.sqrt(b * 2 + c * 2)

# funktsioon round vajab siin kahte argumenti
print("Ristküliku diagonaal", round(di, 2))

print()

print("Ringi karakteristikud")

# float cast oli puudu
r = input("Sisesta ringi raadiusi pikkus => ")

if not r.isdigit():
  print("Sisesta number!")
  exit()

r = float(r)

# korrutusmärk oli puudu
d = 2 * r

print("Ringi läbimõõt", d)

# math.pi ei ole funktsioon
S3: float = math.pi * r * 2

print("Ringi pindala", round(S3))

C: float = 2 * math.pi * r

print("Ringjoone pikkus", round(C))
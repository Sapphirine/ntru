# TEST FILE FOR poly.py
# Generates random polynomials and checks them agains numpy functions

from ntru import poly as q
import random as rand
from numpy.polynomial import polynomial as P


rand.seed(2)
print("TESING 10000 CASES...")
for k in range(10000):
    order1 = rand.randint(0, 10)
    order2 = rand.randint(0, 10)
    c1 = [0]*(order1+1)
    c2 = [0]*(order2+1)
    for i in range(len(c1)):
        c1[i] = rand.randint(-5, 5)
    for i in range(len(c2)):
        c2[i] = rand.randint(-5, 5)

    # TESTING ADDITION FUNCTION
    a = P.polyadd(c1, c2).tolist()
    b = q.addPoly(c1, c2)
    if(a != b):
        print("Failed on Case:")
        print("a add b")
        print("a", a)
        print("b", b)
        break

    # TESTING SUBTRACTION FUNCTION
    a = P.polysub(c1, c2).tolist()
    b = q.subPoly(c1, c2)
    if(a != b):
        print("Failed on Case:")
        print("a subtract b")
        print("a", a)
        print("b", b)
        break

    # TESTING MULTIPLICATION FUNCTION
    a = P.polymul(c1, c2).tolist()
    b = q.multPoly(c1, c2)
    if(a != b):
        print("Failed on Case:")
        print("a * b")
        print("a", a)
        print("b", b)
        break

    # TESINGING DIVISION FUNCTION
    if q.trim(c2) == [0]:
        continue
    try:
        [a1, a2] = P.polydiv(c1, c2)
        a1 = q.trim(a1.tolist())
        a2 = q.trim(a2.tolist())
        [b1, b2] = q.divPoly(c1, c2)
        b1 = list(map(float, b1))
        b2 = list(map(float, b2))
        a1 = [round(x, 5) for x in a1]
        a2 = [round(x, 5) for x in a2]
        b1 = [round(x, 5) for x in b1]
        b2 = [round(x, 5) for x in b2]
    except:
        print("BREAKING ON EXCEPTION")
        print("Failed on Case:")
        print("C1", c1)
        print("C2", c2)
        print("a / b")
        print("a", a1, a2)
        print("b", b1, b2)
        break

    if(a1 != b1 or a2 != b2):
        print("Failed on Case:")
        print("a / b")
        print("a", a1, a2)
        print("b", b1, b2)
        print("Was given: ")
        print("c1", c1)
        print("c2", c2)
        break
print("DONE!")

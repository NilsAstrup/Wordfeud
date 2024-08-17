import numpy as np
import matplotlib.pyplot as plt

ordliste = {}
alfabet = "abcdefghijklmnoprstuvwyæøå"
for b in alfabet:
    ordliste[b] = []
for b in alfabet:
    for b2 in alfabet:
        ordliste[b + b2] = []
for b in alfabet:
    for b2 in alfabet:
        for b3 in alfabet:
            ordliste[b + b2 + b3] = []
for b in alfabet:
    for b2 in alfabet:
        for b3 in alfabet:
            for b4 in alfabet:
                ordliste[b + b2 + b3 + b4] = []

with open("nsf2021.txt", "r") as infile:
    for line in infile:
        k = 0
        if 1 < len(line) < 17:
            i = 0
            if "Ã" in line:
                for n in range(len(line) - 1):
                    if line[n - i] == "Ã" and line[n + 1 - i] == "¦":
                        line = line[: n - i] + "æ" + line[n + 2 - i :]
                        i += 1
                    if line[n - i] == "Ã" and line[n + 1 - i] == "¸":
                        line = line[: n - i] + "ø" + line[n + 2 - i :]
                        i += 1
                    if line[n - i] == "Ã" and line[n + 1 - i] == "¥":
                        line = line[: n - i] + "å" + line[n + 2 - i :]
                        i += 1
            if (
                not ("q" in line)
                and not ("x" in line)
                and not ("z" in line)
                and not ("Ã" in line)
            ):
                if len(line) > 4:
                    ordliste[line[:4]] = ordliste[line[:4]] + [line[:-1]]
                if len(line) == 4:
                    ordliste[line[:3]] = ordliste[line[:3]] + [line[:-1]]
                if len(line) == 3:
                    ordliste[line[:2]] = ordliste[line[:2]] + [line[:-1]]
                else:
                    ordliste[line[0]] = [line[:-1]]
import itertools

ty = input("Hva slags ordspill spiller dere? ")
Brett = {}
for n in range(-7, 8):
    for i in range(-7, 8):
        Brett[(n, i)] = (1, 1)
if ty == "ordspill":
    Brett[(-7, -7)] = (3, 1)
    Brett[(-5, -5)] = (3, 1)
    Brett[(-1, -1)] = (3, 1)
    Brett[(-4, -7)] = (1, 3)
    Brett[(-7, -4)] = (1, 3)
    Brett[(-6, -6)] = (1, 2)
    Brett[(-3, -3)] = (1, 2)
    Brett[(-4, -4)] = (2, 1)
    Brett[(-2, -2)] = (2, 1)
    Brett[(-2, -5)] = (2, 1)
    Brett[(-5, -2)] = (2, 1)
    Brett[(-1, -4)] = (2, 1)
    Brett[(-4, -1)] = (2, 1)
    Brett[(-6, 0)] = (1, 2)
    Brett[(0, -6)] = (1, 2)
    Brett[(-3, 0)] = (2, 1)
    Brett[(0, -3)] = (2, 1)

if ty == "wordfeud":
    Brett[(-7, -7)] = (3, 1)
    Brett[(-4, -4)] = (3, 1)
    Brett[(-2, -2)] = (3, 1)
    Brett[(-6, -2)] = (3, 1)
    Brett[(-2, -6)] = (3, 1)

    Brett[(-3, -7)] = (1, 3)
    Brett[(-7, -3)] = (1, 3)

    Brett[(-5, -5)] = (1, 2)
    Brett[(-3, -3)] = (1, 2)
    Brett[(-4, 0)] = (1, 2)
    Brett[(0, -4)] = (1, 2)

    Brett[(-6, -6)] = (2, 1)
    Brett[(-3, -1)] = (2, 1)
    Brett[(-1, -3)] = (2, 1)
    Brett[(-1, -5)] = (2, 1)
    Brett[(-5, -1)] = (2, 1)
    Brett[(-7, 0)] = (2, 1)
    Brett[(0, -7)] = (2, 1)


for key in Brett:
    if key[0] <= 0 and key[1] <= 0:
        Brett[(-key[0], -key[1])] = Brett[key]
        Brett[(-key[0], key[1])] = Brett[key]
        Brett[(key[0], -key[1])] = Brett[key]


def verdi(bokstav):
    if bokstav in "ABCDEFGHIJKLMNOPRSTUVYWÆØÅ":
        return 0
    if ty == "ordspill":
        if bokstav in ["a", "d", "e", "n", "r", "s", "t"]:
            return 1
        elif bokstav in ["f", "i", "m", "l", "o"]:
            return 2
        elif bokstav in ["h", "k", "g"]:
            return 3
        elif bokstav in ["b", "j", "p", "u"]:
            return 4
        elif bokstav in ["v", "ø", "å"]:
            return 5
        elif bokstav in ["y", "æ"]:
            return 7
        elif bokstav == "w":
            return 9
        elif bokstav == "c":
            return 10
        elif bokstav == "" or bokstav == "x":
            return 0
    else:
        if bokstav in ["a", "d", "e", "n", "r", "s", "t"]:
            return 1
        elif bokstav in ["f", "i", "m", "l"]:
            return 2
        elif bokstav in ["h", "k", "o"]:
            return 3
        elif bokstav in ["b", "j", "p", "u", "g", "å", "ø"]:
            return 4
        elif bokstav in ["v"]:
            return 5
        elif bokstav in []:
            return 7
        elif bokstav in ["y", "æ"]:
            return 8
        elif bokstav in []:
            return 9
        elif bokstav in ["c", "w"]:
            return 10
        elif bokstav == "" or bokstav == "x":
            return 0


B = {}
for key in Brett:
    B[key] = ""
B1 = B.copy()


def posisjon(ord, startposisjon, retning, Bokstaver):
    p = []
    ant = 0
    j = 0
    if retning == "ned":
        while ant < len(ord):
            if startposisjon[1] - j >= -7:
                if Bokstaver[(startposisjon[0], startposisjon[1] - j)] == "":
                    p.append((startposisjon[0], startposisjon[1] - j))
                    ant += 1
                j += 1
            else:
                ant = len(ord) + 1
    if retning == "høyre":
        while ant < len(ord):
            if startposisjon[0] + j <= 7:
                if Bokstaver[(startposisjon[0] + j, startposisjon[1])] == "":
                    p.append((startposisjon[0] + j, startposisjon[1]))
                    ant += 1
                j += 1
            else:
                ant = len(ord) + 1
    return p


def poeng(ord, startposisjon, retning, Bok):

    posisjoner = posisjon(ord, startposisjon, retning, Bok)
    p = 0
    Bokstaver = Bok.copy()
    if len(ord) == 1:
        if startposisjon[0] + 1 <= 7 and startposisjon[0] - 1 >= -7:
            if (
                Bokstaver[startposisjon[0] + 1, startposisjon[1]] != ""
                or Bokstaver[startposisjon[0] - 1, startposisjon[1]] != ""
            ):
                retning = "høyre"
            else:
                retning = "ned"
        elif (
            startposisjon[0] + 1 > 7
            and Bokstaver[startposisjon[0] - 1, startposisjon[1]] != ""
        ):
            retning = "høyre"
        elif (
            startposisjon[0] - 1 < -7
            and Bokstaver[startposisjon[0] + 1, startposisjon[1]] != ""
        ):
            retning = "høyre"
        else:
            retning = "ned"
    if retning == "ned":
        for i in range(len(ord)):
            Bokstaver[posisjoner[i]] = ord[i]
            if not (posisjoner[0][0] == 7 or posisjoner[0][0] == -7):
                if (
                    Bokstaver[posisjoner[i][0] + 1, posisjoner[i][1]] != ""
                    or Bokstaver[posisjoner[i][0] - 1, posisjoner[i][1]] != ""
                ):
                    p += (
                        verdi(ord[i])
                        * Brett[posisjoner[i]][0]
                        * Brett[posisjoner[i]][1]
                    )
                    a = "s"
                    j = 1
                    while a != "":
                        if posisjoner[i][0] + j <= 7:
                            a = Bokstaver[posisjoner[i][0] + j, posisjoner[i][1]]
                        else:
                            a = ""

                        p += verdi(a) * Brett[posisjoner[i]][1]
                        j += 1
                    j = 1
                    a = "s"
                    while a != "":
                        if posisjoner[i][0] - j >= -7:
                            a = Bokstaver[posisjoner[i][0] - j, posisjoner[i][1]]
                        else:
                            a = ""
                        p += verdi(a) * Brett[posisjoner[i]][1]
                        j += 1
            elif (
                posisjoner[0][0] == 7
                and Bokstaver[posisjoner[i][0] - 1, posisjoner[i][1]] != ""
            ):
                p += verdi(ord[i]) * Brett[posisjoner[i]][0] * Brett[posisjoner[i]][1]
                j = 1
                a = "s"
                while a != "":
                    if posisjoner[i][0] - j >= -7:
                        a = Bokstaver[posisjoner[i][0] - j, posisjoner[i][1]]
                    else:
                        a = ""
                    p += verdi(a) * Brett[posisjoner[i]][1]
                    j += 1
            elif (
                posisjoner[0][0] == -7
                and Bokstaver[posisjoner[i][0] + 1, posisjoner[i][1]] != ""
            ):
                p += verdi(ord[i]) * Brett[posisjoner[i]][0] * Brett[posisjoner[i]][1]
                j = 1
                a = "s"
                while a != "":
                    if posisjoner[i][0] + j <= 7:
                        a = Bokstaver[posisjoner[i][0] + j, posisjoner[i][1]]
                    else:
                        a = ""
                    p += verdi(a) * Brett[posisjoner[i]][1]
                    j += 1
        j = 0
        p2 = 0
        b = "yo"
        while b != "":
            pos = posisjoner[0][0], posisjoner[0][1] + j
            b = Bokstaver[pos]
            if pos in posisjoner:
                p2 += verdi(b) * Brett[pos][0]
            else:
                p2 += verdi(b)
            j += 1
            if posisjoner[0][1] + j > 7:
                b = ""
        j = 1
        b = "yo"
        if posisjoner[0][1] - j < -7:
            b = ""
        while b != "":
            pos = posisjoner[0][0], posisjoner[0][1] - j
            b = Bokstaver[pos]
            if pos in posisjoner:
                p2 += verdi(b) * Brett[pos][0]
            else:
                p2 += verdi(b)
            j += 1
            if posisjoner[0][1] - j < -7:
                b = ""

        for pos in posisjoner:
            if Brett[pos][1] == 2:
                p2 = p2 * 2
            elif Brett[pos][1] == 3:
                p2 = p2 * 3
        p += p2

    elif retning == "høyre":
        for i in range(len(ord)):
            Bokstaver[posisjoner[i]] = ord[i]
            if not (posisjoner[0][1] == 7 or posisjoner[0][1] == -7):
                if (
                    Bokstaver[posisjoner[i][0], posisjoner[i][1] + 1] != ""
                    or Bokstaver[posisjoner[i][0], posisjoner[i][1] - 1] != ""
                ):

                    p += (
                        verdi(ord[i])
                        * Brett[posisjoner[i]][0]
                        * Brett[posisjoner[i]][1]
                    )
                    a = "s"
                    j = 1
                    while a != "":
                        if posisjoner[i][1] + j <= 7:
                            a = Bokstaver[posisjoner[i][0], posisjoner[i][1] + j]
                        else:
                            a = ""
                        p += verdi(a) * Brett[posisjoner[i]][1]
                        j += 1

                    j = 1
                    a = "s"
                    while a != "":
                        if posisjoner[i][1] - j >= -7:
                            a = Bokstaver[posisjoner[i][0], posisjoner[i][1] - j]
                        else:
                            a = ""
                        p += verdi(a) * Brett[posisjoner[i]][1]
                        j += 1
            elif (
                posisjoner[0][1] == 7
                and Bokstaver[posisjoner[i][0], posisjoner[i][1] - 1] != ""
            ):
                p += verdi(ord[i]) * Brett[posisjoner[i]][0] * Brett[posisjoner[i]][1]
                j = 1
                a = "s"
                while a != "":
                    if posisjoner[i][1] - j >= -7:
                        a = Bokstaver[posisjoner[i][0], posisjoner[i][1] - j]
                    else:
                        a = ""
                    p += verdi(a) * Brett[posisjoner[i]][1]
                    j += 1
            elif (
                posisjoner[0][1] == -7
                and Bokstaver[posisjoner[i][0], posisjoner[i][1] + 1] != ""
            ):
                p += verdi(ord[i]) * Brett[posisjoner[i]][0] * Brett[posisjoner[i]][1]
                j = 1
                a = "s"
                while a != "":
                    if posisjoner[i][1] + j <= 7:
                        a = Bokstaver[posisjoner[i][0], posisjoner[i][1] + j]
                    else:
                        a = ""
                    p += verdi(a) * Brett[posisjoner[i]][1]
                    j += 1
        j = 0
        p2 = 0
        b = "yo"
        while b != "":
            pos = posisjoner[0][0] + j, posisjoner[0][1]
            b = Bokstaver[pos]
            if pos in posisjoner:

                p2 += verdi(b) * Brett[pos][0]
            else:

                p2 += verdi(b)
            j += 1
            if posisjoner[0][0] + j > 7:
                b = ""
        j = 1
        b = "yo"
        if posisjoner[0][0] - j < -7:
            b = ""
        while b != "":
            pos = posisjoner[0][0] - j, posisjoner[0][1]
            b = Bokstaver[pos]
            if p in posisjoner:
                p2 += verdi(b) * Brett[pos][0]
            else:
                p2 += verdi(b)
            j += 1
            if posisjoner[0][0] - j < -7:
                b = ""

        for pos in posisjoner:
            if Brett[pos][1] == 2:
                p2 = p2 * 2
            elif Brett[pos][1] == 3:
                p2 = p2 * 3

        p += p2
    if len(ord) == 7:
        p += 40
    return p


def trekk(ord, startposisjon, retning, Bokstaver):
    posisjoner = posisjon(ord, startposisjon, retning, Bokstaver)
    for i in range(len(posisjoner)):
        Bokstaver[posisjoner[i]] = ord[i]
    return Bokstaver


# æ=Ã¦ ,   ø=Ã¸ ,    å =Ã¥
alfabet = "abcdefghijklmnopqrstuvwæøå"


def convert(l):
    str = ""
    for e in l:
        str += e
    return str


def permute(ord):
    p = []
    if "x" in ord:
        for X in "AE":
            for b in range(len(ord)):
                if ord[b] == "x":
                    orde = ord[:b] + X + ord[b + 1 :]
            for i in range(1, len(ord) + 1):
                p += itertools.permutations(orde, i)
        s = []
        for e in p:
            e = convert(e)
            # if not(e in s):
            s.append(convert(e))
    else:
        for i in range(1, len(ord) + 1):
            p += itertools.permutations(ord, i)
        s = []
        for e in p:
            e = convert(e)
            if not (e in s):
                s.append(convert(e))

    return s


def ordet(ord, startposisjon, retning, Bokstaver):
    brikker = trekk(ord, startposisjon, retning, Bokstaver.copy())
    ordet = ""
    if retning == "høyre":
        i = 0
        b = "yay"
        while b != "":
            ordet += brikker[startposisjon[0] + i, startposisjon[1]]
            i += 1
            if startposisjon[0] + i <= 7:
                b = brikker[startposisjon[0] + i, startposisjon[1]]
            else:
                b = ""
        i = 1
        b = "yay"
        while b != "":
            if startposisjon[0] - i >= -7:
                s = startposisjon[0] - i, startposisjon[1]
                b = brikker[s]
                ordet = b + ordet
                i += 1
            else:
                b = ""

    if retning == "ned":
        i = 0
        b = "yay"
        while b != "":
            ordet += brikker[startposisjon[0], startposisjon[1] - i]
            i += 1
            if startposisjon[1] - i >= -7:
                b = brikker[startposisjon[0], startposisjon[1] - i]
            else:
                b = ""
        i = 1
        b = "yay"
        while b != "":
            if startposisjon[1] + i <= 7:
                s = startposisjon[0], startposisjon[1] + i
                b = brikker[s]
                ordet = b + ordet
                i += 1
            else:
                b = ""
    return ordet


def kompliment(retning):
    if retning == "høyre":
        return "ned"
    if retning == "ned":
        return "høyre"


"""
ordliste=[]
with open("nsf2021.txt", "r") as infile:
    for line in infile:
        k=0
        if 1<len(line)<13:
            i=0
            for n in range(len(line)-1):
                if line[n-i]=="Ã" and line[n+1-i]=="¦":
                    line= line[:n-i]+"æ"+ line[n+2-i:]
                    i+=1
                if line[n-i]=="Ã" and line[n+1-i]=="¸":
                    line= line[:n-i]+"ø"+ line[n+2-i:]
                    i+=1
                if line[n-i]=="Ã" and line[n+1-i]=="¥":
                    line= line[:n-i]+"å"+ line[n+2-i:]
                    i+=1
            ordliste.append(line[:-1])
"""


def ord_lov(ord, startposisjon, retning, Bokstaver):

    if retning == "høyre":
        k = 0
        for i in range(8 - startposisjon[0]):
            if Bokstaver[startposisjon[0] + i, startposisjon[1]] == "":
                k += 1
        if len(ord) > k:
            return False

    if retning == "ned":
        k = 0
        for i in range(abs(-8 - startposisjon[1])):
            if Bokstaver[startposisjon[0], startposisjon[1] - i] == "":
                k += 1
        if len(ord) > k:
            return False
    if len(ord) < len(ordet(ord, startposisjon, retning, Bokstaver)):
        return True
    else:
        pos = posisjon(ord, startposisjon, retning, Bokstaver)
        if B1 == Bokstaver:
            for e in pos:
                if e == (0, 0):
                    return True
        for e in range(len(ord)):
            word = ordet(ord[e], pos[e], kompliment(retning), Bokstaver)
            if len(word) > 1:
                return True
    return False


def letters(ord, Bokstaver):
    L = {}
    L_brukt = {}
    alfabet = "abcdefghijklmnoprstuvwyæøåx"
    ant_bokstaver = [
        7,
        3,
        1,
        5,
        9,
        4,
        4,
        3,
        6,
        2,
        4,
        5,
        3,
        6,
        4,
        2,
        7,
        7,
        7,
        3,
        3,
        1,
        1,
        1,
        2,
        2,
        2,
    ]
    for i, j in zip(alfabet, ant_bokstaver):
        L[i] = j
        L_brukt[i] = 0
    for pos in Bokstaver:
        if Bokstaver[pos] != "":
            if Bokstaver[pos].lower() == Bokstaver[pos]:
                L_brukt[Bokstaver[pos]] += 1
            else:
                L_brukt["x"] += 1
    for b in ord:
        L_brukt[b] += 1

    gjenværende = {}
    for i in alfabet:
        gjenværende[i] = L[i] - L_brukt[i]

    return gjenværende


def mulige_trekk(ord, startposisjon, retning, Bokstaver, P):

    P2 = {}
    for e in range(len(P)):
        if ord_lov(P[e], startposisjon, retning, Bokstaver) == True:
            o_new = ordet(P[e], startposisjon, retning, Bokstaver)
            P2[e] = o_new

    Muligheter = []
    muligheter = []

    if len(P2) > 0:
        for e in P2:
            p = P2[e]
            pl = p.lower()
            if len(p) == 1:
                if pl in ordliste[pl]:
                    Muligheter.append(P[e])
            elif len(p) == 2:
                if pl in ordliste[pl]:
                    Muligheter.append(P[e])
            elif len(p) == 3:
                if pl in ordliste[pl]:
                    Muligheter.append(P[e])
            else:
                if pl in ordliste[pl[:4]]:
                    Muligheter.append(P[e])

        for i in Muligheter:
            k = 0
            pos = posisjon(i, startposisjon, retning, B)
            for e in range(len(i)):
                if k != 1:
                    word = ordet(i[e], pos[e], kompliment(retning), B)
                    wl = word.lower()
                    if len(word) == 2:
                        if not (wl in ordliste[wl]):
                            k = 1

                    if len(word) == 3:
                        if not (wl in ordliste[wl]):
                            k = 1
                    if len(word) > 3:
                        if not (wl in ordliste[wl[:4]]):
                            k = 1
            if k == 0:
                muligheter.append(i)

    return muligheter


def Max(ord, Bokstaver, D):
    P = permute(ord)

    if ord.lower() != ord:
        bare_x = []
        for o in P:
            if o.lower() != o:
                bare_x.append(o)
        P = bare_x
    Høyre = {}
    Ned = {}
    Muligheter = {}
    if Bokstaver == B1:
        for pos in Bokstaver:
            j = 0
            for retning in ["høyre", "ned"]:
                if retning == "høyre":

                    for i in range(min([7, 8 - pos[0]])):
                        if (pos[0] + i, pos[1]) == (0, 0):
                            j = 1
                            break
                    if not ((ord, pos, retning) in D) and j == 1:

                        mh = mulige_trekk(ord, pos, retning, Bokstaver, P)
                        Høyre[pos] = mh
                        print(pos)
                        print(Høyre[pos])

                if retning == "ned":
                    j = 0
                    for i in range(min([7, abs(-8 - pos[1])])):
                        if (pos[0], pos[1] - i) == (0, 0):
                            j = 1
                            break
                    if not ((ord, pos, "ned") in D) and j == 1:
                        mn = mulige_trekk(ord, pos, "ned", Bokstaver, P)
                        Ned[pos] = mn
                        print(Ned[pos])
    else:

        for pos in Bokstaver:

            if Bokstaver[pos] == "":
                j = 0
                print(pos)
                for retning in ["høyre", "ned"]:
                    if retning == "høyre":

                        if pos[0] != -7:
                            if Bokstaver[pos[0] - 1, pos[1]] != "":
                                j = 1
                        for i in range(min([7, 8 - pos[0]])):
                            if Bokstaver[pos[0] + i, pos[1]] != "":
                                j = 1
                                break
                            if pos[1] + 1 <= 7:
                                if Bokstaver[pos[0] + i, pos[1] + 1] != "":
                                    j = 1
                                    break
                            if pos[1] - 1 >= -7:
                                if Bokstaver[pos[0] + i, pos[1] - 1] != "":
                                    j = 1
                                    break
                        if not ((ord, pos, retning) in D) and j == 1:

                            mh = mulige_trekk(ord, pos, retning, Bokstaver, P)
                            Høyre[pos] = mh
                            print(Høyre[pos])

                    if retning == "ned":
                        j = 0
                        if pos[1] != 7:
                            if Bokstaver[pos[0], pos[1] + 1] != "":
                                j = 1
                        for i in range(min([7, abs(-8 - pos[1])])):
                            if Bokstaver[pos[0], pos[1] - i] != "":
                                j = 1
                                break
                            if pos[0] + 1 <= 7:
                                if Bokstaver[pos[0] + 1, pos[1] - i] != "":
                                    j = 1
                                    break
                            if pos[0] - 1 >= -7:
                                if Bokstaver[pos[0] - 1, pos[1] - i] != "":
                                    j = 1
                                    break
                        if not ((ord, pos, "ned") in D) and j == 1:
                            mn = mulige_trekk(ord, pos, "ned", Bokstaver, P)
                            Ned[pos] = mn
                            print(Ned[pos])
    for p in Høyre:
        for i in Høyre[p]:
            trekk = (i, p, "høyre")
            Muligheter[trekk] = poeng(i, p, "høyre", Bokstaver)
    for p in Ned:
        for i in Ned[p]:
            trekk = (i, p, "ned")
            Muligheter[trekk] = poeng(i, p, "ned", Bokstaver)

    Sortert_tuppel = sorted(Muligheter.items(), key=lambda item: item[1])
    Sortert = {k: v for k, v in Sortert_tuppel}
    if Sortert != {}:
        beste_trekk = Sortert_tuppel[-1][0]
        max_score = Sortert_tuppel[-1][1]
    else:
        beste_trekk = "ingenting"
        max_score = 0
    return Sortert, beste_trekk, max_score


def antall(Bokstaver, ord):
    k = 0
    for i in Bokstaver:
        if Bokstaver[i] != "":
            k += 1
    ant = 104 - k - len(ord)
    return ant


def lage(trekkene, Bokstaver):
    for trekk in trekkene:
        o = trekk[0]
        s = trekk[1]
        r = trekk[2]
        Bokstaver = trekk(o, s, r, Bokstaver)
    return Bokstaver


def Brettet(B):
    for i in range(-7, 8):
        print("")
        str = ""
        for j in range(-7, 8):
            if B[(j, -i)] != "":
                str += f"{B[(j, -i)]}    "
            else:
                str += ".    "
        print(str)


from math import *


def spill(Bokstaver):
    ord = input("Hvilke bokstaver har du? ")
    D = {}
    if "x" in ord:
        uten_x = ""
        for e in ord:
            if "x" != e:
                uten_x += e
        t = Max(uten_x, Bokstaver, D)
        for key in t[0]:
            D[key] = t[0][key]
        for X in "ABCDEFGHIJKLMNOPRSTUVYWÆØÅ":
            for b in range(len(ord)):
                if ord[b] == "x":
                    orde = ord[:b] + X + ord[b + 1 :]

            t = Max(orde, Bokstaver, D)
            for key in t[0]:
                D[key] = t[0][key]
            print(X)
        Sortert_tuppel = sorted(D.items(), key=lambda item: item[1])
        Sortert = {k: v for k, v in Sortert_tuppel}
        beste_trekk = Sortert_tuppel[-1][0]
        max_score = Sortert_tuppel[-1][1]
        a = input("Vil du ha hint? ")
        if a in ["ja", "j", "Ja", "yes", "Yes"]:
            beste_trekk = t[1]
            max_score = t[2]
            input(f"Scoren på det beste ordet er {max_score} ")
            if beste_trekk[1][0] >= 0 and beste_trekk[1][1] >= 0:
                k = 1
            elif beste_trekk[1][0] <= 0 and beste_trekk[1][1] >= 0:
                k = 2
            elif beste_trekk[1][0] <= 0 and beste_trekk[1][1] <= 0:
                k = 3
            elif beste_trekk[1][0] >= 0 and beste_trekk[1][1] <= 0:
                k = 4
            input(f"Første bokstav er i kvadrant nr.{k} ")
            Bokstaver2 = Bokstaver.copy()
            B2 = trekk(beste_trekk[0], beste_trekk[1], beste_trekk[2], Bokstaver2)
            for pos in Bokstaver2:
                if Bokstaver2[pos] == "" and B2[pos] != "":
                    if Brett[pos] == (1, 3):
                        input(f"Du kan få bruk for et trippeltord ")
                    if Brett[pos] == (1, 2):
                        input(f"Du kan få bruk for et dobbeltord ")
                    if Brett[pos] == (3, 1):
                        input(f"Du kan få bruk for en trippelbokstav ")
                    if Brett[pos] == (2, 1):
                        input(f"Du kan få bruk for en dobbelbokstav ")
            input(f"Du skal bruke {len(beste_trekk[0])} bokstaver ")
            input(
                f"Lengden på det totale ordet er {len(ordet(beste_trekk[0], beste_trekk[1], beste_trekk[2], Bokstaver))} "
            )
            import random

            P = permute(beste_trekk[0])
            p = []
            for e in P:
                if len(e) == len(beste_trekk[0]):
                    p.append(e)

            input(f"Du får bruk for bokstavene {random.choice(p)} ")
            input(f"Retning: {beste_trekk[2]} ")
            input(f"Startposisjonen er {beste_trekk[1]} ")
        for element in Sortert:
            print(f"{element}: {Sortert[element]} ")
        input(f"Beste trekk er {beste_trekk}")
    else:
        t = Max(ord, Bokstaver, D)
        a = input("Vil du ha hint? ")
        if a in ["ja", "j", "Ja", "yes", "Yes"]:
            beste_trekk = t[1]
            max_score = t[2]
            input(f"Scoren på det beste ordet er {max_score} ")
            if beste_trekk[1][0] >= 0 and beste_trekk[1][1] >= 0:
                k = 1
            elif beste_trekk[1][0] <= 0 and beste_trekk[1][1] >= 0:
                k = 2
            elif beste_trekk[1][0] <= 0 and beste_trekk[1][1] <= 0:
                k = 3
            elif beste_trekk[1][0] >= 0 and beste_trekk[1][1] <= 0:
                k = 4
            i = 0
            j = 0
            k2 = 0
            l = 0
            Bokstaver2 = Bokstaver.copy()
            B2 = trekk(beste_trekk[0], beste_trekk[1], beste_trekk[2], Bokstaver2)
            for pos in Bokstaver:
                if Bokstaver[pos] == "" and B2[pos] != "":
                    if Brett[pos] == (1, 3) and i == 0:
                        input(f"Du kan få bruk for et trippeltord ")
                        i = 1
                    if Brett[pos] == (1, 2) and j == 0:
                        input(f"Du kan få bruk for et dobbeltord ")
                        j = 1
                    if Brett[pos] == (3, 1) and k2 == 0:
                        input(f"Du kan få bruk for en trippelbokstav ")
                        k2 = 1
                    if Brett[pos] == (2, 1) and l == 0:
                        input(f"Du kan få bruk for en dobbelbokstav ")
                        l = 1

            input(f"Du skal bruke {len(beste_trekk[0])} bokstaver ")
            input(
                f"Lengden på det totale ordet er {len(ordet(beste_trekk[0], beste_trekk[1], beste_trekk[2], Bokstaver))} "
            )
            import random

            P = permute(beste_trekk[0])
            p = []
            for e in P:
                if len(e) == len(beste_trekk[0]):
                    p.append(e)

            input(f"Du får bruk for bokstavene {random.choice(p)} ")
            input(f"Retning: {beste_trekk[2]} ")
            input(f"Første bokstav er i kvadrant nr.{k} ")
            input(f"Startposisjonen er {beste_trekk[1]} ")
        for element in t[0]:
            print(f"{element}: {t[0][element]} ")
        input(f"Beste trekk er {t[1]} ")
    L = letters(ord, Bokstaver)
    vokaler = "aeiouyæøå"
    konsonanter = "bcdfghjklmnprstvw"
    s1 = 0
    s2 = 0
    s3 = 0
    if L["x"] != 0:

        b = "x"
        s3 += L[b]
        print(f"x: {L[b]}")
    print(" ")
    for e in vokaler:
        a = L[e]
        s1 += a
        if a != 0:
            print(f"{e}: {a}")
    print("")
    for e in konsonanter:
        a = L[e]
        s2 += a
        if a != 0:
            print(f"{e}: {a}")
    print(
        f"Antall vokaler: {s1}, Antall konsonanter: {s2}, Antall bokstaver: {s1 + s2 + s3}"
    )
    a = 0
    for b in ord:
        if b in vokaler or b == "x":
            a += 1
    a = len(ord) - a
    x = np.arange(a + 1)
    width = 1
    px = np.zeros(len(x))
    for e in x:
        px[e] = comb(s1 + s3, e) * comb(s2, a - e) / comb(s1 + s2 + s3, a)

    plt.bar(x, px, width, edgecolor="black")
    plt.xlabel("Ant. vokaler")
    plt.ylabel("Punktsannsynlighet")
    plt.show()

    bok = input("Hvor mange bokstaver kunne du eventuelt tenke deg å bytte?")
    x = np.arange(int(bok) + 1)
    width = 1
    px = np.zeros(len(x))
    for e in x:
        px[e] = comb(s1 + s3, e) * comb(s2, int(bok) - e) / comb(s1 + s2 + s3, int(bok))

    plt.bar(x, px, width, edgecolor="black")
    plt.xlabel("Ant. vokaler")
    plt.ylabel("Punktsannsynlighet")

    plt.show()


def o(ord):

    if ord in ordliste[ord]:
        print(f"Ja, {ord} er et ord")
    else:
        print(f"Nei, {ord} er ikke i ordlisten!")


# Tobias:
B = trekk("voldt", (0, 4), "ned", B)
B = trekk("bges", (-1, 3), "høyre", B)
B = trekk("omMeltå", (1, 0), "høyre", B)
B = trekk("brene", (7, 1), "ned", B)
B = trekk("fjea", (-3, 2), "høyre", B)
B = trekk("", (), "", B)


# mamma:


Brettet(B)
spill(B)


"""
L = letters("ijsud", B)
vokaler="aeiouyæøå"
konsonanter="bcdfghjklmnprstvw"
s1=0
s2=0
s3=0
if L["x"]!=0:

    b = "x"
    s3+=L[b]
    print(f"x: {L[b]}")
print(" ")
for e in vokaler:
    a=L[e]
    s1+=a
    if a!=0:
        print(f"{e}: {a}")
print("")
for e in konsonanter:
    a=L[e]
    s2+=a
    if a!=0:
        print(f"{e}: {a}")
print(f"Antall vokaler: {s1}, Antall konsonanter: {s2}, Antall bokstaver: {s1 + s2 + s3}")
"""

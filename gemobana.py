from random import randint, choice

yourlife = 5


gartyma = []


dafa4 = [
          "a1","a2","a3","a4","a5","a6","a7","a8",
          "b1","b2","b3","b4","b5","b6","b7","b8",
          "c1","c2","c3","c4","c5","c6","c7","c8",
          "d1","d2","d3","d4","d5","d6","d7","d8",
          "e1","e2","e3","e4","e5","e6","e7","e8",
          "f1","f2","f3","f4","f5","f6","f7","f8",
          "g1","g2","g3","g4","g5","g6","g7","g8",
          "h1","h2","h3","h4","h5","h6","h7","h8"
      ]

dafa2 = [
          "a1","a2","a3","a4","a5","a6","a7","a8",
          "b1","b2","b3","b4","b5","b6","b7","b8",
          "c1","c2","c3","c4","c5","c6","c7","c8",
          "d1","d2","d3","d4","d5","d6","d7","d8",
          "e1","e2","e3","e4","e5","e6","e7","e8",
          "f1","f2","f3","f4","f5","f6","f7","f8",
          "g1","g2","g3","g4","g5","g6","g7","g8",
          "h1","h2","h3","h4","h5","h6","h7","h8"
      ]
nasroli1 = []

gemi = []

y = 0

while y < 5:
    jj = choice(dafa4)
    gemi.append(jj)
    dafa2.remove(jj)
    y += 1








dafabot = [
          "a1","a2","a3","a4","a5","a6","a7","a8",
          "b1","b2","b3","b4","b5","b6","b7","b8",
          "c1","c2","c3","c4","c5","c6","c7","c8",
          "d1","d2","d3","d4","d5","d6","d7","d8",
          "e1","e2","e3","e4","e5","e6","e7","e8",
          "f1","f2","f3","f4","f5","f6","f7","f8",
          "g1","g2","g3","g4","g5","g6","g7","g8",
          "h1","h2","h3","h4","h5","h6","h7","h8"
      ]




botlife = 5
gemibot = []
nasrolibot = []
y1 = 0

while y1 < 5:
    jj = choice(dafa4)
    gemibot.append(jj)
    dafa2.remove(jj)
    y1 += 1







while True:

    qq = choice(dafabot)
    nasrolibot.append(qq)
    dafabot.remove(qq)








    dafa = [
        "a1","a2","a3","a4","a5","a6","a7","a8",
        "b1","b2","b3","b4","b5","b6","b7","b8",
        "c1","c2","c3","c4","c5","c6","c7","c8",
        "d1","d2","d3","d4","d5","d6","d7","d8",
        "e1","e2","e3","e4","e5","e6","e7","e8",
        "f1","f2","f3","f4","f5","f6","f7","f8",
        "g1","g2","g3","g4","g5","g6","g7","g8",
        "h1","h2","h3","h4","h5","h6","h7","h8"
    ]


    asoebi = ["a", "b", "c", "d", "e", "f", "g", "h"]
    o = 0
    a = ""
    for i in dafa:
        if i in gemi:
            cell = "⛵"
        elif i in nasrolibot:
            cell = "✴️"
        else:
            cell = "⬜"
        if o == 7:
            p = asoebi[0]
            a += cell + p + "\n"
            o = 0
            asoebi.remove(p)
        else:

            a += cell
            o += 1
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" 1 2 3 4  5 6 7 8 ")
    print(a)

    asoebi1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    o1 = 0
    a1 = ""

    if qq in gemi:
        gemi.remove(qq)
        yourlife -= 1

    for i in dafa:
        if i in nasroli1:
            cell1 = "✴️"
        elif i in gartyma:
            cell1 = "✅"
        else:
            cell1 = "⬜"
        if o1 == 7:
            p1 = asoebi1[0]
            a1 += cell1 + p1 + "\n"
            o1 = 0
            asoebi1.remove(p1)
        else:
            a1 += cell1
            o1 += 1

    print(" 1 2 3 4  5 6 7 8 ")
    print(a1)

    while True:

        srola = input("sad isvri? -----> " )
        if srola in nasroli1:
            print("mand uive isrole ")
        elif srola not in dafa:
            print("eg ragaa")
        else:
            if srola in gemibot:
                gartyma.append(srola)
            else:
                nasroli1.append(srola)
            break

    if srola in gemibot:
        gartyma.append(srola)
        botlife -= 1




    if botlife == 0:
        print("SHEN MOIGE, SAGOL TO")
        break

    if yourlife == 0:
        print("WAAGE RAGAS ELODEBI")
        break


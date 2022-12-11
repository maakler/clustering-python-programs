def järjesta_punktid(p):
    indeks = 0
    for n in range(len(p)):
        counter = 0
        for i in p:
            counter += 1
            indeks = p.index(i)
            if counter == len(p):
                break
            elif i[1] > p[indeks+1][1]:
                suurem = p[indeks]
                vaiksem = p[indeks + 1]
                p[indeks] = vaiksem
                p[indeks + 1] = suurem
            elif i[1] == p[indeks+1][1]:
                if i[0] > p[indeks+1][0]:
                    suurem = p[indeks]
                    vaiksem = p[indeks + 1]
                    p[indeks] = vaiksem
                    p[indeks + 1] = suurem
def järjesta_punktid(koordinaadid):
    for i in range(len(koordinaadid)):
        min = i
        for j in range(i+1, len(koordinaadid)):
            if koordinaadid[j][1] < koordinaadid[min][1]:
                min = j
            elif koordinaadid[j][1] == koordinaadid[min][1]:
                if koordinaadid[j] < koordinaadid[min]:
                    min = j
        if i != min:
            koordinaadid[i], koordinaadid[min] = koordinaadid[min], koordinaadid[i]
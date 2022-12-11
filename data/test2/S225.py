def järjesta_punktid(koordinaadid):
    for i in range(len(koordinaadid)):
        väikseim = i
        for j in range(i+1, len(koordinaadid)):
            if koordinaadid[j][1] == koordinaadid[väikseim][1]:
                if koordinaadid[j][0] < koordinaadid[väikseim][0]:
                    väikseim = j
            if koordinaadid[j][1] < koordinaadid[väikseim][1]:
                väikseim = j
        if i != väikseim:
            koordinaadid[i], koordinaadid[väikseim] = koordinaadid[väikseim], koordinaadid[i]

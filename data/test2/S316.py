def järjesta_punktid(punktid):
    for i in range(len(punktid)):
        for j in range(i+1,len(punktid)):
            if punktid[i][0] > punktid[j][0]:
                punktid[i], punktid[j] = punktid[j], punktid[i]
            if punktid[i][1] > punktid[j][1]:
                punktid[i], punktid[j] = punktid[j], punktid[i]
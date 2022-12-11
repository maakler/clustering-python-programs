def järjesta_punktid(järjend):
    for i in range(len(punktid)):
        for j in range(len(punktid)):
            if punktid[i][0]>punktid[j][0]:
                punktid[i], punktid[j]=punktid[j], punktid[i]
            if punktid[i][1]>punktid[j][1]:
                punktid[i], punktid[j]=punktid[j], punktid[i]
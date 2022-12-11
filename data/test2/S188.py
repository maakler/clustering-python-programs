def järjesta_punktid(punktid):
    for k in range(len(punktid)):
        minimaalne = punktid[k:][0]
        for i in range(len(punktid[k:])):
            if punktid[k:][i][1] < minimaalne[1]:
                minimaalne = punktid[k:][i]
            elif punktid[k:][i][1] == minimaalne[1]:
                if punktid[k:][i][0] < minimaalne[0]:
                    minimaalne = punktid[k:][i]
        if minimaalne != punktid[k]:
            punktid[punktid[k:].index(minimaalne) + k] = punktid[k]
            punktid[k] = minimaalne
            
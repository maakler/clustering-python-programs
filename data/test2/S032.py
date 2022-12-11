def järjesta_punktid(punktid):
    algsed_punktid = punktid[:]
    for i in range(len(punktid)-1):
        if punktid[i][1] > punktid[i+1][1]:
            punktid[i], punktid[i+1] = punktid[i+1], punktid[i]
        elif punktid[i][1] == punktid[i+1][1]:
            if punktid[i][0] > punktid[i+1][0]:
                punktid[i], punktid[i+1] = punktid[i+1], punktid[i]
    if punktid == algsed_punktid:
        #return punktid
        punktid
    else:
        järjesta_punktid(punktid)


p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(p)
järjesta_punktid(p)
print(p)

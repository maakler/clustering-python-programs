#https://stackabuse.com/bubble-sort-in-python/

def järjesta_punktid(tlist):
    for i in range(len(tlist)):
        for j in range(len(tlist) - 1):
            alus = 1
            if tlist[j][alus] > tlist[j+1][alus]:
                tlist[j], tlist[j+1] = tlist[j+1], tlist[j]
            if tlist[j][alus] == tlist[j+1][alus]:
                alus = 0
                if tlist[j][alus] > tlist[j+1][alus]:
                    tlist[j], tlist[j+1] = tlist[j+1], tlist[j]
                    
    
list = [(4,1), (3,3), (2,0), (6,1),(1,0), (3,2), (5,2), (1,1)]
järjesta_punktid(list)
print(list)
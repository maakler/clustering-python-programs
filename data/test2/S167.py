#test
#p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
#p = [(1, 4), (6, 4), (4, 4), (3, 4)]
p = [(1, 2), (2, 1)]
#p = [4, 3, 1, 7, 8]

def kontroll(p):
    pikkus = len(p)
    lugeja = 0
    for i in range(0, pikkus - 1):
        if p[i][1] == p[i+1][1]:
            lugeja += 1
    if lugeja == pikkus - 1:
        return True
def järjesta_punktid(p):
    if kontroll(p) == True:
        for i in range(len(p)):
            min = i
            for j in range(i+1, len(p)):
                if p[j][0] < p[min][0]:
                    min = j
            if i != min:
                p[i], p[min] = p[min], p[i]

    else:
        for i in range(len(p)):
            min = i
            for j in range(i+1, len(p)):
                if p[j][1] < p[min][1]:
                    min = j
            if i != min:
                p[i], p[min] = p[min], p[i]

järjesta_punktid(p)
print(p)
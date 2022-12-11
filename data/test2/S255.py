p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(n):
    for i in range(len(n)-1):
        vahetused = 0
        for j in range(len(n)-1):
            if n[j][1] > n[j+1][1]:
                vahetused += 1
                n[j], n[j+1] = n[j+1], n[j]
            if n[j][1] == n[j+1][1] and n[j][0] > n[j+1][0]:
                n[j], n[j+1] = n[j+1], n[j]
                vahetused += 1
        if vahetused == 0:
            break
järjesta_punktid(p)
print(p)
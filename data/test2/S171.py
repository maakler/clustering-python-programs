#bubble sort

def järjesta_punktid(li):

    for i in range(len(li)):
        for j in range(len(li)-i-1):

            if li[j][1] > li[j+1][1]:
                li[j], li[j+1] = li[j+1], li[j]

            elif li[j][1] == li[j+1][1] and li[j][0] > li[j+1][0]:
                li[j], li[j+1] = li[j+1], li[j]



p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)


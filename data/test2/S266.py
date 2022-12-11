# järjesta punktid

def vaiksem(el1, el2):
    #return el1 < el2
    if el1[1] != el2[1]:
        return el1[1] < el2[1]
    else:
        return el1[0] < el2[0]

def järjesta_punktid(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            #if a[j] < a[min]:
            if vaiksem(a[j], a[min]):
                min = j
        if i != min:
            a[i], a[min] = a[min], a[i]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
#p = [3, 5, 7, 1, 2]
järjesta_punktid(p)
#print(p)
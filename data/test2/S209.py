p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def vaiksem_punkt(a,b):
    if a[1] < b[1]:
        return True
    elif a[1] == b[1]:
        return a[0] < b[0]
    else:
        return False


def järjesta_punktid(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if vaiksem_punkt(a[j],a[min]):
                min = j
        if i != min:
            a[i], a[min] = a[min], a[i]

järjesta_punktid(p)
print(p)
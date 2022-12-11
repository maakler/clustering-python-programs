def swap(x):
    return (x[1], x[0])

def järjesta_punktid(p): 
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(p) - 1):
            if swap(p[i]) > swap(p[i + 1]):
                p[i], p[i + 1] = p[i + 1], p[i]
                swapped = True

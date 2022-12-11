def mull(järjend):
    n = len(järjend)
    for i in range(n):
        for j in range(0, n-i-1):
            if järjend[j][0] > järjend[j+1][0] and järjend[j][1] >= järjend[j+1][1]:
                järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
    return järjend
                    
def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min_indeks = i
        for j in range(i + 1, len(järjend)):
            if järjend[min_indeks][1] > järjend[j][1]:
                min_indeks = j
        järjend[i], järjend[min_indeks] = järjend[min_indeks], järjend[i]
    mull(järjend)
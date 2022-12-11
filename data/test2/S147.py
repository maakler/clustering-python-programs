def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min_indeks = i
        for j in range(i+1,len(järjend)):
            if järjend[min_indeks][1] > järjend[j][1]:
                min_indeks = j
            elif järjend[min_indeks][1] == järjend[j][1]:
                if järjend[min_indeks][0] > järjend[j][0]:
                    min_indeks = j
        järjend[i], järjend[min_indeks] = järjend[min_indeks], järjend[i]
    print(järjend)
a = [(4,1), (3,3), (2,0), (6,1), (1,0), (2,3), (3,2), (5,2), (1,1)]
järjesta_punktid(a)
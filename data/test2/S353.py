def järjesta_punktid(järjend):
    for n in range(len(järjend)):
        väikseim = float('inf'), float('inf')
        for indeks, el in enumerate(järjend[n:], start=n):
            if el[1]<väikseim[1] or (el[1]==väikseim[1] and el[0]<väikseim[0]):
                väikseim = el[0], el[1]
                i = indeks
        järjend[n], järjend[i] = järjend[i], järjend[n]
        

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
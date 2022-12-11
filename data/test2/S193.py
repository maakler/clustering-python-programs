# p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
# >>> järjesta_punktid(p)
# >>> print(p)
# [(2, 0), (1, 1), (4, 1), (6, 1), (3, 2), (5, 2), (3, 3)]


def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min = i
        for l in range(i + 1 , len(järjend)):
            if järjend[min][1] > järjend[l][1]:
                min = l
            if järjend[min][1] == järjend[l][1]:
                if järjend [min][0] > järjend[l][0]:
                    min = l
            järjend[min], järjend[i] = järjend[i], järjend[min]
    return järjend

    


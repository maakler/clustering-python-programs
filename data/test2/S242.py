def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min = i
        for j in range(i+1, len(järjend)):
            if järjend[j][1] < järjend[min][1]:
                min = j
            elif järjend[j][1] == järjend[min][1]:
                if j < min:
                    järjend[i], järjend[min] = järjend[min], järjend[i]
        if i != min:
            järjend[i], järjend[min] = järjend[min], järjend[i]
    

järjend = [(2, 0), (1, 1), (4, 1), (6, 1), (3, 2), (5, 2), (3, 3)]
järjesta_punktid(järjend)
print(järjend)
        
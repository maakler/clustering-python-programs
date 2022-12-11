def järjesta_punktid(list):
    for i in range(0, len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j]<list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

list=[(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(list))
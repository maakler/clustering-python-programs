def järjesta_punktid(järjend):
    for i in range(0,len(järjend)-1):
        väikseim=i
        for j in range (i,len(järjend)):
            if järjend[j][1]==järjend[väikseim][1]:
                if järjend[j][0]<järjend[väikseim][0]:
                    väikseim=j
            elif järjend[j][1]<järjend[väikseim][1]:
                väikseim=j
        järjend[i],järjend[väikseim]=järjend[väikseim],järjend[i]
    return järjend
print(järjesta_punktid([(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]))
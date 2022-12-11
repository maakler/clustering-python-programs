def järjesta_punktid(järjend):
    for i in range(10):
        for i in range(2, len(järjend)+1, 1):
            for j in range(len(järjend[0])):
                if järjend[i-2][1] > järjend[i-1][1]:
                    järjend[i-2], järjend[i-1] = järjend[i-1], järjend[i-2]
                if järjend[i-2][1] == järjend[i-1][1] and järjend[i-2][0] > järjend[i-1][0]:
                    järjend[i-2], järjend[i-1] = järjend[i-1], järjend[i-2]
    print(järjend)
järjesta_punktid([(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)])
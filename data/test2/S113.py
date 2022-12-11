def järjesta_punktid(järjend):
    järjendipikkus = len(järjend)
    for i in range(0, järjendipikkus):
        for j in range(0, järjendipikkus-i-1):
            if järjend[j][1] > järjend[j+1][1] or ((järjend[j][0]>järjend[j+1][0]) and (järjend[j][1] == järjend[j+1][1])):
                x = järjend[j]
                järjend[j] = järjend[j+1]
                järjend[j+1] = x
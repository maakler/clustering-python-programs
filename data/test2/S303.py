def järjesta_punktid(jarjend):
    while True:
        sorted = True
        for i in range(len(jarjend)-1):
            if jarjend[i][1] > jarjend[i+1][1]:
                sorted = False
                jarjend[i], jarjend[i+1] = jarjend[i+1], jarjend[i]
            if jarjend[i][1] == jarjend[i+1][1] and jarjend[i][0] > jarjend[i+1][0]:
                sorted = False
                jarjend[i], jarjend[i+1] = jarjend[i+1], jarjend[i]
        if sorted: break

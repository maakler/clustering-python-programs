def järjesta_punktid(jar):
    for i in range(len(jar) - 1):
        for j in range(len(jar) - i - 1):
            if jar[j][1] > jar[j + 1][1]:
                jar[j], jar[j + 1] = jar[j + 1], jar[j]

    for i in range(len(jar) - 1):
        for j in range(len(jar) - i - 1):
            if jar[j][1] == jar[j + 1][1]:
                if jar[j][0] > jar[j + 1][0]:
                    jar[j], jar[j + 1] = jar[j + 1], jar[j]
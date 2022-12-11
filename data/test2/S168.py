def järjesta_punktid(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[j][1] < list[i][1]:
                list[i], list[j] = list[j], list[i]
            elif list[j][1] == list[i][1]:
                if list[j][0] < list[i][0]:
                    list[i], list[j] = list[j], list[i]
                    


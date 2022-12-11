def järjesta_punktid(järjend):
    for i in range(len(järjend)-1):
        mini = i
        for j in range(i+1, len(järjend)):
            if järjend[j][1] < järjend[mini][1]:
                mini = j
            elif järjend[j][1] == järjend[mini][1]:
                if järjend[j][0] < järjend[j][0]:
                    mini = j
        if i != mini:
            järjend[i], järjend[mini] = järjend[mini], järjend[i]
def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        miinimum = i
        for j in range(i+1, len(järjend)):
            if järjend[miinimum] > järjend[j]:
                miinimum = j
        järjend[i], järjend[miinimum] = järjend[miinimum], järjend[i]
        järjend.sort(key=lambda x:x[1])     

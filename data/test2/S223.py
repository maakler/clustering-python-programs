def järjesta_punktid(array):
    for y in range(len(array)-1):
        for x in range(len(array)-y-1):
            if array[x][1] > array[x+1][1]:
                array[x], array[x+1] = array[x+1], array[x]
            elif array[x][1] == array[x+1][1] and array[x][0] > array[x+1][0]:
                array[x], array[x+1] = array[x+1], array[x]
def järjesta_punktid(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx][1] > array[j][1]:
                min_idx = j   
        array[i], array[min_idx] = array[min_idx], array[i]
        
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx][1] == array[j][1]:
                if array[min_idx][0] > array[j][0]: 
                    min_idx = j   
        array[i], array[min_idx] = array[min_idx], array[i]
    
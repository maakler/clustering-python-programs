p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(p):
    sorted_list = []
    for i in range(len(p)):
        min_element = i
        for j in range(i+1, len(p)):
            if p[min_element][1] > p[j][1]:
                if p[min_element][0] > p[j][0]:
                    min_element = j
        p[i], p[min_element] = p[min_element], p[i]
    for i in range(len(p)):
        sorted_list.append(p[i])
    return sorted_list
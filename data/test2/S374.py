def järjesta_punktid(massiiv):
    x_massiiv = []
    y_massiiv = []
    
    for i in range(len(massiiv)):
        y_massiiv.append(massiiv[i][1])
        x_massiiv.append(massiiv[i][0])
        
    uus_massiiv = y_massiiv.copy()
    for i in range(len(massiiv)):
        miinimum = min(uus_massiiv)
        uus_massiiv.remove(miinimum)
        index = y_massiiv.index(miinimum)
        y_massiiv[i], y_massiiv[index] = y_massiiv[index], y_massiiv[i]
        x_massiiv[i], x_massiiv[index] = x_massiiv[index], x_massiiv[i]
        massiiv[i], massiiv[index] = massiiv[index], massiiv[i]
    
    for i in range(len(massiiv)-1):
        if  y_massiiv[i] == y_massiiv[i+1]:
            if x_massiiv[i] > x_massiiv[i+1]:
                x_massiiv[i], x_massiiv[i+1] = x_massiiv[i+1], x_massiiv[i]
                massiiv[i], massiiv[i+1] = massiiv[i+1], massiiv[i]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)
        
    
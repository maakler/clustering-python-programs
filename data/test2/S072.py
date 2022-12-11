def järjesta_punktid(sisend):
    muudatus_tehtud = True
    
    while muudatus_tehtud:
        muudatus_tehtud = False
        
        for i in range(len(sisend) - 1):
            if sisend[i][1] > sisend[i + 1][1] or (sisend[i][1] == sisend[i + 1][1] and sisend[i][0] > sisend[i + 1][0]):
                sisend[i], sisend[i + 1] = sisend[i + 1], sisend[i]
                muudatus_tehtud = True
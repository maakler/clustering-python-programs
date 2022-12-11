# Bubble sort meetod

def järjesta_punktid(koordinaadid):
    vahetatud = True
    kordus = 0
    while (vahetatud):
        vahetatud = False
        for i in range (len(koordinaadid) - kordus - 1): # Y koordinaat
            if koordinaadid[i][1] > koordinaadid[i+1][1]:
                temp = koordinaadid[i]
                koordinaadid[i] = koordinaadid[i+1]
                koordinaadid[i + 1] = temp
                vahetatud = True
            elif koordinaadid[i][1] == koordinaadid[i+1][1]: # X koordinaat
                if koordinaadid[i][0] > koordinaadid[i + 1][0]:
                    temp = koordinaadid[i]
                    koordinaadid[i] = koordinaadid[i+1]
                    koordinaadid[i + 1] = temp
                    vahetatud = True                  
        kordus += 1


                    
        
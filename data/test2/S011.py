#p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(p):
    if len(p) < 2:
        return p
    kesk = len(p)//2
    vasak = järjesta_punktid(p[:kesk])
    parem = järjesta_punktid(p[kesk:])
    return merge(vasak,parem)

def merge(vasak, parem):
    vaste=[] ; i=0 ; j=0
    while (i<len(vasak) and j<len(parem)):
        if vasak[i[0]] < parem[j[0]]:
                vaste.append(vasak[i]); i+=1
        elif vasak[i[0]] == parem[j[0]]:
            if vasak[i[1]] < parem[j[1]]:
                vaste.append(vasak[i]); i+=1
            else:
                vaste.append(parem[j]); j+=1
        else:
            vaste.append(parem[j]); j+=1
    vaste += vasak[i:]
    vaste += parem[j:]
    return vaste

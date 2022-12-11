def järjesta_punktid(koord_järj):
    muutsin = True
    while muutsin:
        muutsin = False
        for i in range(len(koord_järj)-1):
            el1 = koord_järj[i]
            el2 = koord_järj[i+1]
            if el1[1] > el2[1]:
                koord_järj[i] = el2
                koord_järj[i+1] = el1
                muutsin = True
            if el1[1] == el2[1]:
                if el1[0] > el2[0]:
                    koord_järj[i] = el2
                    koord_järj[i+1] = el1
                    muutsin = True
            else:
                continue
    print(koord_järj)
        
    
    

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
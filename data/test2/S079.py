# 2. Järjesta punktid
# Võta aluseks mõne sortimismeetodi (nt valikumeetod (selection sort), mullimeetod (bubble sort),
# pistemeetod (insertion sort)) kood ja tee sellest funktsioon järjesta_punktid, mille parameetriks on
# tasandipunktide koordinaatide järjend ning mis järjestab punktid koordinaatide kasvamise järjekorras ridade kaupa,
# samas reas asuvad punktid veerukaupa. Iga punkti koordinaadid on antud kaheliikmelise ennikuna.
# Funktsioon muudab etteantud järjendit, mitte ei tagasta uut järjendit.

def järjesta_punktid(koordinaadid):
    for i in range(len(koordinaadid)):
        for j in range(len(koordinaadid)):
            if koordinaadid[i][1] < koordinaadid[j][1]:
                koordinaadid[i], koordinaadid[j] = koordinaadid[j], koordinaadid[i]
            elif koordinaadid[i][1] == koordinaadid[j][1]:
                if koordinaadid[i][0] < koordinaadid[j][0]:
                    koordinaadid[i], koordinaadid[j] = koordinaadid[j], koordinaadid[i]
                
    

# p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
#p = [(1,2), (2,1)]
#järjesta_punktid(p)
#print(p) # [(2, 0), (1, 1), (4, 1), (6, 1), (3, 2), (5, 2), (3, 3)]
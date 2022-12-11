'''2. Järjesta punktid
Võta aluseks mõne sortimismeetodi (nt valikumeetod (selection sort),
mullimeetod (bubble sort), pistemeetod (insertion sort)) kood ja tee sellest funktsioon järjesta_punktid,
mille parameetriks on tasandipunktide koordinaatide järjend ning mis järjestab punktid koordinaatide
kasvamise järjekorras ridade kaupa, samas reas asuvad punktid veerukaupa.
Iga punkti koordinaadid on antud kaheliikmelise ennikuna. Funktsioon muudab etteantud järjendit,
mitte ei tagasta uut järjendit.

Näide.

>>> p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
>>> järjesta_punktid(p)
>>> print(p)
[(2, 0), (1, 1), (4, 1), (6, 1), (3, 2), (5, 2), (3, 3)]'''



'''def järjesta_punktid(p):
    #for i in range(len(p)):
    for rida in p:
        a = rida[0]
        b = rida[1]
        #print(a)
        min = i[0]
        for j in range(i+1, len(p)):
            if p[j] < p[min]:
                min = j
            
            if i != min:
                p[1], p[min] = p[min], p[i]'''


'''def järjesta_punktid(p):
    for i in range(len(p)):
        #print(p[i][:1])
        min = i
        for j in range(i+1, len(p)):
            if p[j][:1] < p[min][:1]:
                min = j
            
        if i != min:
            p[1], p[min] = p[min], p[i]'''



def järjesta_punktid(p):
    from operator import itemgetter
    p.sort(key=itemgetter(1,0))
    #return(p)

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
(järjesta_punktid(p))

# koostada funktsioon, mille argumendiks on ennikute järjend
# muudame antud järjendit ja sorteerime kasvavasse järjekorda

def järjesta_punktid(p):
    for i in range(len(p)):
        min = i #seame i-nda elemendi võrreldavaks
        for j in range(i+1, len(p)): # hakkame j-iga edasisi elemente kontrollima
            # esmalt järjestame y-koordinaadi järgi
            if p[j][1] < p[min][1]: #juhul kui leidub element, mis on väiksem, on see uus min
                min = j #min on hetkel leitud väikseim element
        if i != min: #juhul kui leidub väiksem element kui alguses i-ks võetud
            p[i], p[min] = p[min], p[i] #vahetame nende kohad, et väiksem oleks eespool
    # x-koordinaadid on nüüd vaja ka järjestada korduvate y-te puhul
    for i in range(len(p)):
        min=i
        for j in range(i+1, len(p)):
            if p[j][1]!= p[min][1]: # kui y on erinev, siis pole alust sorteerida
                pass
            elif p[i][1]== p[i+1][1]: # kui on võrdsed, peab sorteerima
                if p[min][0]> p[j][0]: # kui eelneva x on suurem, tuleb vahetada ära
                    min= j
        if i != min: #juhul kui leidub väiksem element kui alguses i-ks võetud
                p[i], p[min] = p[min], p[i]
                
            


p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
#p= [3, 5, 1, 7, 2] 

v= järjesta_punktid(p)
print(p)
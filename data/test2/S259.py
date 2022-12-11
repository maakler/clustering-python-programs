def järjesta_punktid(punktid):
    for i in range(len(punktid)): #teeb läbi nii mitu korda, kui list on pikk
        for j in range(len(punktid)-1):
            
            if punktid[j][1] > punktid[j+1][1]: #kui y-koordinaat suurem kui järgmise elemendi oma
                punktid[j], punktid[j+1] = punktid[j+1], punktid[j] #siis vaheta asukohad
                
            elif punktid[j][1] == punktid[j+1][1]: #kui y-koordinaat sama
                if punktid[j][0] > punktid[j+1][0]: #siis kontrollib x-koordinaati
                    punktid[j], punktid[j+1] = punktid[j+1], punktid[j] #ning vahetab uuesti kohad
    print(punktid)
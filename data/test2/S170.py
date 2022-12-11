def järjesta_punktid(tasand):
    palju = range(len(tasand))
    for i in palju:
        for m in palju:
            
            if i == 6 or m == 6:
                return tasand
            if tasand[i][1] == tasand[m + 1][1]:
                if tasand[i][0] > tasand[m + 1][0]:
                    tasand[i], tasand[m + 1] = tasand[m + 1], tasand[i]
                
    return tasand
            
    
    



p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

print(järjesta_punktid(p))
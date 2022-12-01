import turtle as trt

poolikuPaadiJuhend = [["otse",100],
                      ["parem",-45],
                      ["otse",70],
                      ["parem",-135],
                      ["otse",155]]


#joonista kasutades etteantud listi ja töölist
#ning vajadusel võta listist tagurpidi
def drawFromList(instruction, turtle, inverse=False):
    if inverse:
        l = instruction
        p = -1
    else:
        l = instruction
        p = 1
    
    for i in l:
        if i[0] == "otse":
            turtle.forward(i[1]*p)
        if i[0] == "parem":
            turtle.right(i[1]*p)
    
#defineeri töölised
worker1 = trt.Turtle()
worker2 = trt.Turtle()

#joonista ükshaaval
drawFromList(poolikuPaadiJuhend, worker1)
drawFromList(poolikuPaadiJuhend, worker2, True)

trt.exitonclick()
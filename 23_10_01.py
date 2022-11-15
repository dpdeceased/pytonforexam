print("x,y,z,f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((not x) <= (not y)) and ((not(z <= y)))
            print(x,y,z,f)
print("x,y,z,f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((not x) or (y and z)) <= (z == ((not y) and x))
            print(x,y,z,f)
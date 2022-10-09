def dvtr(start, finish):
    if (start > finish):
        return 0
    if (start == finish):
        return 1
    x = dvtr(start + 2, finish)
    y = dvtr(start * 4, finish)
    z = dvtr(start + 1, finish)
    return x+y+z
print(dvtr(2,25))
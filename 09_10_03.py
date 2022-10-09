def f(start, finish):
    if (start > finish):
        return 0
    if (start == finish):
        return 1
    x = f(start+3, finish)
    y = f(start*2, finish)
    z = f(start+1, finish)
    return x+y+z
print(f(2,10) * f(10,30))
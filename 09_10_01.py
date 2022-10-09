def f(start, finish):
    if (start > finish):
        return 0
    if (start == finish):
        return 1
    x = f(start + 1, finish)
    y = f(start + 10, finish)
    return x + y
print(f(7, 49))
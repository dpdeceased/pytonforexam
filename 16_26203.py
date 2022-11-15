def f(n):
    if (n < 3):
        return n
    if (n > 2):
        return f(n - 1) * f(n - 3) + 2 * f(n - 2)


print(f(6))

def is_prime(n):
    for j in range(2, int(n**0.5)+1):
        if (n % j == 0):
            return False
    return True

def count_div(n):
    k = 0
    for j in range(1, n+1):
        if (n % j == 0 ):
            k = k + 1
    return k

def find_div(n):
    a = []
    for j in range(1, int(n**0.5)+1):
        if (n%j==0):
            a.append(j)
            if (j != n//j):
                a.append(n//j)
    a.sort()
    return a
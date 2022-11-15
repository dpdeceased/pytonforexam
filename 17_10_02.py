s = '4'*88
while '444' in s or '11' in s:
    if('444' in s):
        s = s.replace('444','1',1)
    else:
        s = s.replace('11','4',1)
print(s)
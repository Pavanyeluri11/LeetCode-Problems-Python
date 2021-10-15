def xorOperation(n,start):
    c=0
    for i in range(n):
        c^=(start+2*i)
    return c

print(xorOperation(5,2))


def blevers(n1):
    c = 0
    c1 = 1
    while c1 <= n1:
        while n1 % c1 == 0:
            c += 1
        c1 += 1
    print(c1)
    return c % 100


n = blevers(15)

print(n)

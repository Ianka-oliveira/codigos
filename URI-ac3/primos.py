n1 = int(input())
n2 = int(input())

arrayPrimos = []
i = 0

for x in range(n1, n2+1):
    t = 0

    for y in range(1, x+1):
        if x % y == 0:
            t += 1

    if t <= 2 and t != 1:
        arrayPrimos.append(x)

qtd = len(arrayPrimos)

while i < len(arrayPrimos):
    print(arrayPrimos[i])
    i += 1
print(f'primos: {qtd}')

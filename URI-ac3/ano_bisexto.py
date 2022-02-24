anoInicio = int(input())
anoFim = int(input())
i = 0

for ano in range(anoInicio, anoFim+1):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano)
        i += 1


print(f'bissextos: {i}')

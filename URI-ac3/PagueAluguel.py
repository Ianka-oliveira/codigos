divida = int(input())
vrComprometido = int(input())
i = 0

while i <= divida:
    if i == 0 and (vrComprometido <= 0 or divida <= 0):
        break
    calc = divida - vrComprometido

    if calc <= 0:
        calc = 0
    i += 1
    print("pagamento:", i)
    print("antes =", divida)
    print("depois =", calc)
    print("-----")
    divida = divida - vrComprometido

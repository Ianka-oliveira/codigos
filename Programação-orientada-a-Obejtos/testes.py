
from calendar import c


def eh_primo(n):
    aux = 0
    for c in range(1, n + 1):
        if n % c == 0:
            aux += 1
    if aux == 2:
        return True
    else:
        return False


def lista_primos(n):
    lista = []
    for i in range(2, n):
        if eh_primo(i):
            lista.append(i)
    return lista


def conta_primos(s):
    listaP = []
    p = {}
    for i in s:
        if eh_primo(i):
            listaP.append(i)

    for i in listaP:
        p[i] = listaP.count(i)

    return p


conta_primos([11, 2, 3, 4, 11, 2, 5, 2])


def eh_armstrong(n):
    digit = 0
    sum = 0
    pot = len(str(n))
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** pot
        temp //= 10
    if n == sum:
        return True
    else:
        return False


def eh_quase_armstrong(n):
    sum = 0
    pot = len(str(n))
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** pot
        temp //= 10

    if sum == n - 1 or sum == n + 1:
        return True
    else:
        return False


def lista_armstrong(n):
    lista = []
    for i in range(n):
        if eh_armstrong(i):
            lista.append(i)
    return lista


def eh_perfeito(n):
    soma = 0
    for a in range(1, n):
        if n % a == 0:
            soma += a
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for i in range(2, n):
        if eh_perfeito(i):
            lista.append(i)
    return lista


class Televisao:

    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco


# Programa Principal
tv1 = Televisao("Samsung", 2500.0)  # testeac2
tv2 = Televisao("LG", 3700.0)

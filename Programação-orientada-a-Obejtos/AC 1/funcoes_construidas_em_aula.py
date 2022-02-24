def eh_primo(n):
    qtd_divisores = 0  # conta quantos divisores n possui
    candidato = 1
    while candidato <= n:
        if n % candidato == 0:    # testando se n é divisível por candidato
            qtd_divisores += 1
        candidato += 1
    if qtd_divisores == 2:
        return True
    else:
        return False


def lista_primos(n):
    lista = []
    for i in range(2, n):   # i varia de 2 até n-1
        if eh_primo(i):    # testa se i é um número primo
            # adiciona i ao final da lista, se i for um número primo
            lista.append(i)
    return lista


def conta_primos(s):
    numero = 2
    divisores = 0

    while (numero <= n-1):
        if n % numero == 0:
            divisores = divisores + 1
    if (divisores == 0):
        else:

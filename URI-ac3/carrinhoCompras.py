'''
ENTRADA

 -  A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha em branco;

 -  Cada linha seguinte conterá um dos comandoss listados acima e, para os comandoss "adicionar" e "remover", conterá também o código de um produto separado por um espaço;

 -  A entrada termina sempre com o comandos "encerrar".

SAIDA

 -  A exibição dos códigos na lista, separados por espaço, de acordo com a execução dos comandoss "exibir" e "encerrar";
 -  A mensagem "código <código> não encontrado", quando o comandos remover é executado com um código que não esteja presente na lista.
    Substitua <código> pelo número do código em questão (veja os exemplos para maiores detalhes)

REGRAS

-   adicionar: inclui o código de um novo produto à lista;
-   remover: remove o código de um produto da lista;
-   exibir: exibe os itens da lista em ordem crescente;
-   encerrar: exibe os itens da lista, assim como no comandos exibir, em ordem crescente, e encerra o programa.

'''

carrinho = [int(x) for x in input().split()]


def exibir():
    carrinho.sort()
    for i in carrinho:
        print(i, end=" ")


def adicionar(item):
    carrinho.append(item)


def remover(item):
    if item in carrinho:
        carrinho.remove(item)
    else:
        print(f" código {item} não encontrado ")


flag = True
aux = []
comandos = []

while flag:

    comandos = list(input().split())

    if "adicionar" in comandos[0] and len(comandos) == 2:
        aux.extend(comandos)
    elif "remover" in comandos[0] and len(comandos) == 2:
        aux.extend(comandos)
    elif "exibir" in comandos[0] and len(comandos) == 1:
        aux.extend(comandos)
    elif "encerrar" in comandos:
        aux.extend(comandos)
        break


for i in range(len(aux)):

    if "encerrar" not in aux[i]:
        valor = aux[i+1]

    if "exibir" in aux[i]:
        exibir()
    elif "adicionar" in aux[i] and valor.isdigit():
        item = int(valor)
        adicionar(item)
    elif "remover" in aux[i] and valor.isdigit():
        item = int(valor)
        remover(item)
    elif "encerrar" in aux[i]:
        exibir()
        break

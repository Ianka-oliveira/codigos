'''
PROBLEMA

    Como Forrest está muito ocupado ultimamente, planejando como cumprir uma promessa a um antigo amigo que adorava restaurantes e camarão, 
    pediu a você que crie um programa que receba 
    como entrada os tempos das corridas que estão nos papeis e calcule a média aritmética dos tempos gastos 
    por ele para completar o seu percurso de corrida diário. 
    Ao final, seu programa deve também exibir todos os tempos de corrida abaixo dessa média, 
    na mesma ordem em que foram recebidos na entrada.


ENTRADA

    - Diversos valores inteiros, um por linha, que representam os tempos gastos em cada corrida (em segundos);
    - A entrada é finalizada com a inserção de um valor negativo, que não deve ser contabilizado.

SAIDA

    - Na primeira linha a palavra 'MEDIA', sem apóstrofos, sem acentuação e completamente em maiúsculo, 
    seguida por dois pontos (':'), 
    um caractere de espaço e um valor real com duas casas decimais, 
    indicando a média dos tempos dados na entrada, em segundos;

    - Nas linhas seguintes, os tempos de corrida abaixo da média calculada, em segundos, 
    um por linha e na mesma ordem em que foram dados na entrada.

'''

# entrada
flag = True
listValor = []
valor = 0

while flag:

    valor = int(input())

    if valor < 0:
        break

    listValor.append(valor)

media = sum(listValor) / len(listValor)


# saida
print("MEDIA: {:.2f}".format(media))

for i in listValor:
    if i < media:
        print(i)

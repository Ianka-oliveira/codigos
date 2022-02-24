'''
PROBLEMA

    Para possibilitar a premiação, cada registro da tabela terá quatro campos dispostos em colunas na seguinte ordem:

    O nome do canal;

    A quantidade atual de inscritos;
    A monetização do último mês do canal e;

    Um valor indicando se o canal produz conteúdo premium,
    que são vídeos exclusivos para usuários que pagam uma mensalidade à ImpacTube.

    Você foi escolhido para desenvolver um programa que receberá como entrada os dados de cada canal,
    gerando internamente a tabela modelo, e que mostrará os nomes dos canais, na ordem em que foram dados na entrada,
    acompanhados do valor que receberão como bonificação.
    Observe cuidadosamente o formato de entrada e o formato de saída especificados.

ENTRADA

    Na primeira linha será informado um número inteiro
    que representa a quantidade N (1 <= N <= 200) de canais da tabela;

    Em cada uma das N linhas seguintes serão informados os registros que compõem a tabela,
    com os valores das colunas separados por um ponto e vírgula,
    nesta ordem:
        (1) uma string com o nome do canal que será bonificado;
        (2) um número natural que é a quantidade de inscritos no canal;
        (3) um número real simbolizando a monetização do canal no mês anterior (dado em reais R$) e;
        (4) uma string 'sim' ou 'não',
        sem apóstrofos e completamente em minúsculo, que indica se o canal produz conteúdo premium;

    Por fim, serão informados dois números reais X e Y, um em cada linha,
    que indicam o valor fixo (em reais R$) que os canais receberão a mais para cada mil inscritos no canal.
    O primeiro valor é X e refere-se aos canais que possuem conteúdo premium.
    O segundo valor é Y e refere-se aos canais que não possuem conteúdo premium.

SAIDA

    O cabeçalho contém três linhas,  sendo a primeira e a terceira compostas por apenas cinco hifens,
    e a segunda composta unicamente pela palavra 'BÔNUS', sem apóstrofos e completamente em maiúsculo.
    Nas próximas N linhas, estão os nomes dos canais, na mesma ordem em que foram dados na entrada,
    acompanhados à direita pelo valor que receberão como bonificação,
    em reais e com duas casas decimais, exatamente como consta nos exemplos.


'''
# entrada
# N(1 <= N <= 200)
qtdCanais = int(input())

if qtdCanais == 0 or qtdCanais > 200:
    exit()

listaCanais = []

i = 0
while i < qtdCanais:

    infoCanais = list(input().split(";"))
    listaCanais.extend(infoCanais)
    i += 1


bonusSim = float(input())
bonusNao = float(input())


def calculoMonet(premium):

    if premium == "sim":
        bonus = bonusSim
    else:
        bonus = bonusNao

    resto = int(qtdInscritos/1000)

    if resto >= 1:
        calcInscritos = (resto*bonus)
        calcInscritos = calcInscritos + monetizacao
    else:
        calcInscritos = monetizacao

    return calcInscritos


print("-" * 5)
print("BÔNUS")
print("-" * 5)

t = 0
varCanal = 0
varInscritos = 1
varMonet = 2
varPremium = 3

while t < qtdCanais:

    nomeCanal = listaCanais[varCanal]
    qtdInscritos = float(listaCanais[varInscritos])
    monetizacao = float(listaCanais[varMonet])
    premium = listaCanais[varPremium]

    resultado = calculoMonet(premium)

    print("{}: R$ {:.2f}".format(nomeCanal, resultado))

    varCanal += 4
    varInscritos += 4
    varMonet += 4
    varPremium += 4
    t += 1

'''
PROBLEMA

    Você se voluntariou para implementar esse software, 
    que precisa receber um valor inicial indicando a quantidade de alunos da turma, 
    seguido pelas notas originais de cada aluno e pelas notas obtidas na nova atividade. 
    O programa deverá exibir a quantidade de alunos que tiveram suas notas alteradas, 
    assim como as notas originais e finais de cada aluno, destacando aqueles que aumentaram as notas.


ENTRADA

    - Na primeira linha haverá um número natural N (1 <= N <= 999) indicando a quantidade de alunos da turma;
    - Nas próximas N linhas, haverá a nota original de cada aluno, que são valores reais no intervalo fechado [ 0,10 ];
    - Por fim, nas N linhas seguintes, haverá a nota obtida na nova atividade por cada aluno, 
      também situadas no intervalo fechado [ 0,10 ].

    Note que as N primeiras notas correspondem as notas originais dos N primeiros alunos, 
    e as próximas N notas correspondem as notas da "Segunda Chance" dos mesmos alunos.
    Portanto, se N = 5, a 1ª nota é do primeiro aluno e a 6ª nota também é do primeiro aluno (original e "Segunda Chance), 
    a 2ª nota é do segundo aluno e a 7ª também, a 5ª é do quinto aluno e a 10ª também.
   
SAIDA

    - A primeira linha será a frase 'NOTAS ALTERADAS: <quantidade>', sem apóstrofos e completamente em maiúsculo, 
    em que <quantidade> deve ser substituído pela quantidade de alunos que tiveram suas notas originais alteradas 
    em decorrência da aplicação do bônus;

    - As próximas N linhas serão as notas de todos os alunos, na mesma ordem dada na entrada, 
    iniciando com asterisco ('*') para indicar as notas que foram alteradas e hífen ('-') para indicar aquelas que não foram, 
    seguido pela posição da referida nota entre parênteses. 
    O formato de cada linha pode ser observada nos exemplos. 

    Onde se destacam três características: 
        -- (I) a posição tem sempre três dígitos, completada com zeros à esquerda quando necessário; 
        -- (II) todas as notas são exibidas com duas casas decimais e; 
        -- (III) todas as notas ocupam cinco colunas, incluindo o caractere ponto, 
        e completadas com zeros à esquerda quando necessário.

'''

# entradas
qtdAlunos = int(input())

if qtdAlunos < 1 or qtdAlunos > 999:
    exit()

i = 0
notas = float()
listaNotas = []

while i < qtdAlunos:
    notas = float(input())

    if notas < 0 or notas > 10:
        exit()
    else:
        listaNotas.append(notas)

    i += 1

i = 0
notaNovaAtividade = float()
listaNovaAtiv = []

while i < qtdAlunos:

    notaNovaAtividade = float(input())

    if notaNovaAtividade < 0 or notaNovaAtividade > 10:
        exit()
    else:
        listaNovaAtiv.append(notaNovaAtividade)

    i += 1


# saidas
i = 0
qtdNotasAlt = 0

while i < qtdAlunos:
    if listaNovaAtiv[i] == 10 and listaNotas[i] != 10:
        qtdNotasAlt += 1
    i += 1


print(f"NOTAS ALTERADAS: {qtdNotasAlt}")

i = 0
contador = 1
while i < qtdAlunos:

    if listaNovaAtiv[i] == 10 and listaNotas[i] != 10:
        novaNota = float(listaNotas[i] + 2)

        if novaNota > 10:
            novaNota = 10

        print("*({}) original: {:05.2F} | final: {:05.2F}".format(
            str(contador).zfill(3), listaNotas[i], novaNota))
    else:
        print("-({}) original: {:05.2F} | final: {:05.2F}".format(
            str(contador).zfill(3), listaNotas[i], listaNotas[i]))

    i += 1
    contador += 1

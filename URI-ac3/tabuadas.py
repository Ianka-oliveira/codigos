'''
PROBLEMA:
    Escreva um programa que receba como entrada dois números inteiros 
    quaisquer A e B e exiba todas as tabuadas existentes no intervalo fechado crescente [ A..B ].

ENTRADA
    Dois números inteiros, um em cada linha.

SAIDA
    As tabuadas de todos os valores inteiros no intervalo fechado crescente [ A..B ]. 
    Ao fim de cada tabuada, exibir uma linha com dez hifens ('-'). 
    Caso A seja maior do que B, o intervalo será vazio e, neste caso, 
    deve ser exibida somente a frase 'Nenhuma tabuada no intervalo!', 
    sem apóstrofos. Obs.: Lembre-se de não exibir texto no input.

'''
a = int(input())
b = int(input())

if a > b:
    print("Nenhuma tabuada no intervalo!")

for i in range(a, b+1):

    for t in range(1, 11):
        print(f"{i} x {t} = {i * t}")

    print("-" * 10)

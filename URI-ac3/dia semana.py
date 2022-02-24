dia = input()
entrega = int(input())

lista = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
indice = lista.index(dia)

#nova_lista = lista[indice:7] + lista[0:indice]
#dia_entrega = nova_lista[entrega]
if entrega == 0:
    print('chega hoje!')
else:
    print('sera entregue', lista[indice-1])

# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
num = int(input('Informe um número:'))
antecessor = num - 1
sucessor = num + 1
print('O antecessor é {}'.format(antecessor))
print('O sucessor é {}'.format(sucessor))

# Crie um algoritmo que leia um número e mostre o seu dobre triplo e raiz quadrada
num = int(input('Informe outro número:'))
dobro = num * 2
triplo = num * 3
raiz = num**4
print('O dobro de {} é {}'.format(num, dobro))
print('O triplo de {} é {}'.format(num, triplo))
print('A raiz quadrada de {} é {}'.format(num, raiz))

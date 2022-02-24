print("Digite um numero natural")
n = int(input())

if (n % 2) == 0:
    par = n + 2
    impar = n - 1
else:
    par = n + 1
    impar = n - 2

print(impar, par)
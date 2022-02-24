print("*********")
print("Bem Vindo ao Jogo de Adivinhação!")
print("*********")

numero_secreto = 42

chute_str = input("Digite o seu número!: ")

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print(" Você errou! o seu chute foi maior do que o número secreto")
    if (chute < numero_secreto):
        print("Você errou o seu chute!, pois foi menor do que seu número secreto")

print("Fim de Jogo")

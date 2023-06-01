import random


print("*******************************************")
print("Bem vindo ao jogo de Adivinhação no Python!")
print("*******************************************")

numero_secreto = random.randrange(1,101) # 0.0 1.0
total_de_tentativas = 0
pontos = 1000

print("Qual é o seu nivel de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
print("Lembre-se que so pode colcar numeros de 1 a 100!!!")
print("**************************************************")


nivel = int(input("Defina seu nível aqui: "))
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print(f"Tentativas {rodada} de {total_de_tentativas}")

    print("***********************************************")
    chute_str = input("Digite o seu número aqui: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)
    if chute < 1 or chute > 100:
        print("Você deve digitar um numero entra 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print(f"Parabéns voce acertou e fez {pontos} pontos!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")
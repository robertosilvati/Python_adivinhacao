
def jogar():
    print("*************************************")
    print("Bem vindo ao jogo de Forca em Python!")
    print("*************************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    
    print(letras_acertadas)

    enforcou = False
    acertou = False
    #enquanto não enforcou E não acertou
    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar()
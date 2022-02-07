"""

Objetivo: implementar um simplificado jogo da forca

Projeto 5 de 
https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

"""

import random

palavras = ["banana",
"abacate",
"pera",
"uva",
"morango",
"escola",
"otorrinolaringologista"]

tentativas = 4
vitoria = False

palavra_forca = palavras[random.randint(0, len(palavras) - 1)]

palavra_forca_hash = ['.' for word in palavra_forca]

print(palavra_forca_hash)

print("A palavra tem %d letras" % (len(palavra_forca)))

try:
    while(tentativas > 0 and not vitoria):
        option = int(input("Adivinhar palavra? (1 - Sim | 0 - Não): "))
        if(option == 1):
            palavra = input("Qual a palavra? ")
            if(palavra == palavra_forca):
                vitoria = True
            else:
                tentativas = 0
        else:
            letra = input("Qual letra? ")
            letra = letra[0]
            if(letra in palavra_forca):
                print("A letra %c está contida na palavra" % (letra))
                for i in range(len(palavra_forca)):
                    if(letra == palavra_forca[i]):
                        palavra_forca_hash[i] = letra
                print(palavra_forca_hash)
            else:
                tentativas -= 1
                print("A letra %c não está contida na palavra." % (letra))
                print("Você possui mais %d tentativas..." % (tentativas))

    if (vitoria):
        print("Parabens! Voce ganhou!")
    else:
        print("Game Over. Tente mais uma vez! :)")
except:
    print("Ocorreu um erro. Reinicie o jogo.")

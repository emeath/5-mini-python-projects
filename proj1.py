# 10-24 07-07-2020
#
# Projeto 1 - Adivinhe o numero
#
# Objetivo: computador sorteia um número e o usuário deve adivinha-lo
#

from random import randint

class Game:

    def __init__(self):
        self.computador = Computador()
        self.jogador = Jogador()

        self.computador.sortear_numero()

    def game_loop(self):

        while True:
            self.solicitar_numero_jogador()

            # Verifica se o jogador ganhou, caso nao, computador da dica
            if self.win():
                break

            else:
                self.computador.dica_para_jogador(self.jogador.numero)

    def solicitar_numero_jogador(self):
        print('Tente adivinha um numero de 0 a 100: ', end='')
        self.jogador.adivinhar_numero()

    def win(self):
        if self.jogador.numero == self.computador.numero:
            print("Voce venceu!")
            # indica que jogador acertou
            return True
        else:
            # indica que jogador nao acertou
            return False

class Computador:

    def sortear_numero(self):
        self.numero = randint(0, 100)
        print('numero sorteado: {}'.format(self.numero))

    def dica_para_jogador(self, numero_jogador):
        if numero_jogador <= self.numero - 20 or \
                numero_jogador >= self.numero + 20:
            print("Muito frio!")
        elif numero_jogador <= self.numero - 10 or \
                numero_jogador >= self.numero + 10:
            print("Frio!")
        elif numero_jogador <= self.numero - 5 or \
                numero_jogador >= self.numero + 5:
            print("Quente!")
        elif numero_jogador <= self.numero - 2 or \
                numero_jogador <= self.numero + 2:
            print("Muito quente!")

class Jogador:

    def adivinhar_numero(self):
        self.numero = input()
        self.numero = int(self.numero)

if __name__ == '__main__':
    game = Game()
    game.game_loop()
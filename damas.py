import os

# função parar limpar console]
fim = False
erro_input = False


def clear(): return os.system('cls')


class jogo:
    def __init__(self):
        # Eixo X   A  B  C  D  E  F  G  H
        self.arena = [[2, 0, 2, 0, 2, 0, 2, 0],
                      [0, 2, 0, 2, 0, 2, 0, 2],
                      [2, 0, 2, 0, 2, 0, 2, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0], ]

        self.campo_x_inicial = None
        self.campo_y_inicial = None

        self.campo_x_destino = None
        self.campo_y_destino = None

        self.jogador = 2

        self.turno = 1

        self.regra_jogador = None

        self.placar = [[1, 0], [2, 0]]

    pass

    def muda_jogadores(self):
        if self.jogador == 2:
            self.jogador = 1
        else:
            self.jogador = 2

    def print_arena(self):
        print("====== Pontos ======")
        for y in range(0, len(self.placar)):
            print('Jogador:', self.placar[y][0],
                  '|| Pontos:', self.placar[y][1])
        print('\n\n')
        print("   A  B  C  D  E  F  G  H")
        for n in range(0, len(self.arena)):
            print(n, self.arena[n])

    def posicao_inicial(self):
        print("------- Escolha sua peça! -------")
        mssg = "Jogador '" + str(self.jogador) + "' Digite a Letra da coluna: "
        self.campo_x_inicial = str(input(mssg)).upper()
        if self.campo_x_inicial == 'A':
            self.campo_x_inicial = 0
        elif self.campo_x_inicial == 'B':
            self.campo_x_inicial = 1
        elif self.campo_x_inicial == 'C':
            self.campo_x_inicial = 2
        elif self.campo_x_inicial == 'D':
            self.campo_x_inicial = 3
        elif self.campo_x_inicial == 'E':
            self.campo_x_inicial = 4
        elif self.campo_x_inicial == 'F':
            self.campo_x_inicial = 5
        elif self.campo_x_inicial == 'G':
            self.campo_x_inicial = 6
        elif self.campo_x_inicial == 'H':
            self.campo_x_inicial = 7
        else:
            invalid = "'"+str(self.campo_x_inicial) + \
                "' Letra da coluna invalida!"
            print(invalid)
            erro_input = True
            return 0

        erro_input = False
        mssg = "Jogador '" + str(self.jogador) + "' Digite o Número da linha: "
        self.campo_y_inicial = int(input(mssg))
        if self.campo_y_inicial > 0 and self.campo_y_inicial > 7:
            invalid = "'"+str(self.campo_y_inicial) + \
                "' Número da linha invalida! "
            erro_input = True
            print(invalid)
            return 0
        erro_input = False

    def posicao_final(self):
        print("------- Escolha para onde sua peça irá! -------")
        mssg = "Jogador '" + str(self.jogador) + "' Digite a Letra da coluna: "
        self.campo_x_destino = str(input(mssg)).upper()
        if self.campo_x_destino == 'A':
            self.campo_x_destino = 0
        elif self.campo_x_destino == 'B':
            self.campo_x_destino = 1
        elif self.campo_x_destino == 'C':
            self.campo_x_destino = 2
        elif self.campo_x_destino == 'D':
            self.campo_x_destino = 3
        elif self.campo_x_destino == 'E':
            self.campo_x_destino = 4
        elif self.campo_x_destino == 'F':
            self.campo_x_destino = 5
        elif self.campo_x_destino == 'G':
            self.campo_x_destino = 6
        elif self.campo_x_destino == 'H':
            self.campo_x_destino = 7
        else:
            invalid = "'"+str(self.campo_x_destino) + \
                "' Letra da coluna invalida!"
            erro_input = True
            print(invalid)

        erro_input = False
        mssg = "Jogador '" + str(self.jogador) + "' Digite o Número da linha: "
        self.campo_y_destino = int(input(mssg))
        if self.campo_y_destino > 0 and self.campo_y_destino > 7:
            invalid = "'"+str(self.campo_y_destino) + \
                "' Número da linha invalida!"
            print(invalid)
            erro_input = True
            return 0

        erro_input = False

    def validar_posicao_inicial(self):
        if self.jogador == 1:
            self.regra_jogador = [1, 1, 2]
        elif self.jogador == 2:
            self.regra_jogador = [2, -1, 1]

    def regra(self):
        if self.arena[self.campo_y_inicial][self.campo_x_inicial] == self.regra_jogador[0]:
            # se posição inicial for igual a jogador, continuar
            if self.arena[self.campo_y_destino][self.campo_x_destino] != self.regra_jogador[0] and self.arena[self.campo_y_destino][self.campo_x_destino] != 0:
                # se posição final for diferente de eu mesmo e diferente de 0, continuar
                if self.arena[self.campo_y_destino][self.campo_x_destino] == self.regra_jogador[2]:
                    # se posição final for igual ao jogador oponente, continuar
                    self.arena[self.campo_y_inicial][self.campo_x_inicial] = 0
                    self.arena[self.campo_y_destino][self.campo_x_destino] = self.regra_jogador[0]
                    for n in range(0, len(self.placar)):
                        if self.placar[n][0] == self.jogador:
                            self.placar[n][1] += 1
                            if self.placar[n][1] == 12:
                                fim = True
                                mssg = "Jogador " + \
                                    str(self.regra_jogador[0]
                                        )+' é o ganhador!'
                                print(mssg)
            elif self.arena[self.campo_y_destino][self.campo_x_destino] == 0:
                # se campo destino for igual a 0, movimentar para
                self.arena[self.campo_y_destino][self.campo_x_destino] = self.regra_jogador[0]
                self.arena[self.campo_y_inicial][self.campo_x_inicial] = 0
                print(self.arena)
                # substinui a peça e adiciona ponto ao placar
        else:
            print("Jogador não pode escolher esta peça!")


start = jogo()

while True:
    # clear()
    start.muda_jogadores()
    start.print_arena()
    start.posicao_inicial()
    if erro_input == True:
        start.posicao_inicial()
    start.posicao_final()
    if erro_input == True:
        start.posicao_inicial()
    start.validar_posicao_inicial()
    start.regra()
    if fim == True:
        print(mssg)
        break

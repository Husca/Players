import functions_jogo

class Player():  # Classe Mãe
    def __init__(self, nome, clube, altura, assistencias):
        self.nome = nome
        self.clube = clube
        self.altura = altura
        self.assistencias = assistencias

class FutebolPlayer(Player):
    def __init__(self, nome, clube, golos, altura, penalties, assistencias):  # inputs
        super().__init__(nome=nome, clube=clube, altura=altura, assistencias=assistencias)
        self.golos = golos
        self.penalties = penalties

class BasketPlayer(Player):
    def __init__(self, nome, clube, cestos, altura, assistencias):  # inputs
        super().__init__(nome=nome, clube=clube, altura=altura,assistencias=assistencias)
        self.cestos = cestos


# Programa para registo de jogadores
functions_jogo.jogo()
















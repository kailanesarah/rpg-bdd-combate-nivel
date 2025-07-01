class Personagem:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida_max = vida
        self.vida = vida
        self.derrotado = False

    def receber_dano(self, dano):
        if self.derrotado:
            return
        self.vida = max(0, self.vida - dano)
        if self.vida == 0:
            self.derrotado = True

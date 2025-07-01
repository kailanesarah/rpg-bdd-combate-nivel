# src/personagens.py

class PersonagemManager:
    def __init__(self):
        self.missoes_xp = [
            {"nome": "Ajude a idosa a encontrar seu gato", "xp": 14},
            {"nome": "Derrote 3 bandidos", "xp": 10},
            {"nome": "Recupere a pedra mágica", "xp": 20},
            {"nome": "Entregue comida a um sem-teto", "xp": 12},
            {"nome": "Elimine o chefe dos bandidos", "xp": 18},
            {"nome": "Salve a princesa do castelo inimigo", "xp": 150},
            {"nome": "Mate o dragão", "xp": 200},
            {"nome": "Roube o ouro do dragão", "xp": 70}
        ]

        self.niveis_data = [ 
            {"nivel": 1, "xp": 0},
            {"nivel": 2, "xp": 10},
            {"nivel": 3, "xp": 100},
            {"nivel": 4, "xp": 200},
            {"nivel": 5, "xp": 300},
            {"nivel": 6, "xp": 500},
        ]

    def pegar_xp_missao(self, nome_missao):
        for missao in self.missoes_xp:
            if missao['nome'] == nome_missao:
                return missao['xp']
        return None

    def pegar_xp_nivel(self, nivel_personagem):
        for nivel_info in self.niveis_data: 
            if nivel_info['nivel'] == nivel_personagem:
                return nivel_info['xp']
        return None

    def criar_personagem(self, nome, nivel):
        return {
            'nome': nome,
            'nivel': nivel,
            'xp_acumulado': 0
        }

    def tentar_subir_de_nivel(self, personagem, xp_por_nivel):
        xp_acumulado = personagem['xp_acumulado']
        nivel_atual = personagem['nivel']
        novo_nivel = nivel_atual

        for nivel, xp_necessario in xp_por_nivel.items():
            if xp_acumulado >= xp_necessario and nivel > novo_nivel:
                novo_nivel = nivel

        personagem['nivel'] = novo_nivel
        return personagem

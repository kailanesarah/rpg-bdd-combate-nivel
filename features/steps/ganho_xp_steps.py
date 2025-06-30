from behave import given, when, then


missoes_xp = [
    {"nome": "Ajude a idosa a encontrar seu gato", "xp": 14},
    {"nome": "Derrote 3 bandidos", "xp": 10},
    {"nome": "Recupere a pedra mágica", "xp": 20},
    {"nome": "Entregue comida a um sem-teto", "xp": 12},
    {"nome": "Elimine o chefe dos bandidos", "xp": 18},
    {"nome": "Salve a princesa do castelo inimigo", "xp": 150},
    {"nome": "Mate o dragão", "xp": 200},
    {"nome": "Roube o ouro do dragão", "xp": 70}
]


def cria_ou_retorna_personagem(context, nome, nivel, xp):
    if not hasattr(context, 'personagens'):
        context.personagens = {}

        context.personagens[nome] = {
            'nome': nome,
            'nivel': nivel,
            'xp_acumulado': xp
        }
    return context.personagens[nome]


def pegar_xp_missao(nome_missao):
    for missao in missoes_xp:
        if missao['nome'] == nome_missao:
            return missao['xp']
    return None


@given('que o personagem "{nome_personagem}" está no Nível {nivel:d}')
def step_cria_personagem(context, nome_personagem, nivel):
    cria_ou_retorna_personagem(context, nome_personagem, nivel, 0)



@given('"{nome_personagem}" possui {xp:d} de XP acumulado')
def step_personagem_possui_xp(context, nome_personagem, xp):
    if nome_personagem not in context.personagens:
        cria_ou_retorna_personagem(nome_personagem, 1, 0)
    else:
        context.personagens[nome_personagem]['xp_acumulado'] = xp


@given('a missão "{nome_missao}" garante {xp_recompensa:d} de XP')
def step_missao_garante_xp(context, nome_missao, xp_recompensa):
    assert pegar_xp_missao(
        nome_missao) == xp_recompensa, "XP da missão está incorreto"


@when('personagem "{nome_personagem}" completa a missão "{nome_missao}"')
def step_personagem_completa_missao(context, nome_personagem, nome_missao):
    xp_missao = pegar_xp_missao(nome_missao)
    context.personagens[nome_personagem]['xp_acumulado'] += xp_missao


@then('ele deve ter {xp_esperado:d} de XP')
def step_verificar_xp_final(context, xp_esperado):
    for personagem in context.personagens.values():
        assert personagem['xp_acumulado'] == xp_esperado, (
            f"Esperava {xp_esperado}, mas foi {personagem['xp_acumulado']}"
        )

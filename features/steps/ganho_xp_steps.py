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

# Função auxiliar para inicializar o contexto
def inicializa_contexto(context, nome, nivel, xp):
    if not hasattr(context, 'personagens'):
        context.personagens = {}

    if nome not in context.personagens:
        personagem = {
            'nome': nome,
            'nivel': nivel,
            'xp_acumulado': xp
        }
        context.personagens[nome] = personagem

    return context.personagens[nome]


def pegar_xp_missao(nome_missao):
    for missao in missoes_xp:
        if missao['nome'] == nome_missao:
            return missao['xp']
    return None


@given('que o personagem "{nome_personagem}" está no Nível {nivel:d}')
def step_cria_personagem(context, nome_personagem, nivel):
    inicializa_contexto(context, nome_personagem, nivel, 0)


@given('"{nome_personagem}" possui {xp:d} de XP acumulado')
def step_personagem_possui_xp(context, nome_personagem, xp):
    if not hasattr(context, 'personagens'):
        context.personagens = {}

    if nome_personagem not in context.personagens:
        inicializa_contexto(context, nome_personagem, 1, 0)

    context.personagens[nome_personagem]['xp_acumulado'] = xp


@given('a missão "{nome_missao}" garante {xp_recompensa:d} de XP')
def step_missao_garante_xp(context, nome_missao, xp_recompensa):
    xp_real = pegar_xp_missao(nome_missao)
    assert xp_real == xp_recompensa, f"XP da missão está incorreto: esperado {xp_recompensa}, mas é {xp_real}"


@when('personagem "{nome_personagem}" completa a missão "{nome_missao}"')
def step_personagem_completa_missao(context, nome_personagem, nome_missao):
    xp_missao = pegar_xp_missao(nome_missao)
    personagem = context.personagens.get(nome_personagem)
    assert personagem is not None, f"Personagem {nome_personagem} não encontrado"
    personagem['xp_acumulado'] += xp_missao


@then('ele deve ter {xp_esperado:d} de XP')
def step_verificar_xp_final(context, xp_esperado):
    for personagem in context.personagens.values():
        if personagem['xp_acumulado'] == xp_esperado:
            True
            break

    assert personagem[
        'xp_acumulado'] == xp_esperado, f"Nenhum personagem tem o XP esperado {xp_esperado}"

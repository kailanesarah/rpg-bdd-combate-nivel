from behave import given, when, then
from src.personagens import PersonagemManager

manager = PersonagemManager()


def inicializa_contexto(context):
    if not hasattr(context, 'personagens'):
        context.personagens = {}
    if not hasattr(context, 'xp_por_nivel'):
        context.xp_por_nivel = {
            nivel['nivel']: nivel['xp'] for nivel in manager.niveis_data
        }


@given('que o personagem "{nome_personagem}" está no Nível {nivel:d}')
def step_cria_personagem(context, nome_personagem, nivel):
    inicializa_contexto(context)
    context.personagens[nome_personagem] = manager.criar_personagem(
        nome_personagem, nivel)


@given('"{nome_personagem}" possui {xp:d} de XP acumulado')
def step_personagem_possui_xp(context, nome_personagem, xp):
    inicializa_contexto(context)
    context.personagens[nome_personagem]['xp_acumulado'] = xp


@given('a missão "{nome_missao}" garante {xp_recompensa:d} de XP')
def step_missao_garante_xp(context, nome_missao, xp_recompensa):
    inicializa_contexto(context)
    xp_real = manager.pegar_xp_missao(nome_missao)
    assert xp_real == xp_recompensa, f"XP da missão está incorreto: esperado {xp_recompensa}, mas é {xp_real}"


@when('personagem "{nome_personagem}" completa a missão "{nome_missao}"')
def step_personagem_completa_missao(context, nome_personagem, nome_missao):
    inicializa_contexto(context)
    xp_missao = manager.pegar_xp_missao(nome_missao)
    personagem = context.personagens.get(nome_personagem)
    assert personagem is not None, f"Personagem {nome_personagem} não encontrado"
    personagem['xp_acumulado'] += xp_missao


@then('ele deve ter {xp_esperado:d} de XP')
def step_verificar_xp_final(context, xp_esperado):
    inicializa_contexto(context)
    for personagem in context.personagens.values():
        if personagem['xp_acumulado'] == xp_esperado:
            True
            break

    assert personagem[
        'xp_acumulado'] == xp_esperado, f"Nenhum personagem tem o XP esperado {xp_esperado}"

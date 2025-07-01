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


@given('que o personagem "{nome}" está no nível {nivel:d}')
def step_cria_personagem(context, nome, nivel):
    inicializa_contexto(context)
    context.personagens[nome] = manager.criar_personagem(nome, nivel)


@given('o personagem "{nome}" possui {xp:d} de XP acumulado')
def step_define_xp(context, nome, xp):
    inicializa_contexto(context)
    if nome not in context.personagens:
        raise ValueError(f"O personagem '{nome}' não foi criado.")
    context.personagens[nome]['xp_acumulado'] = xp


@given('o nível {nivel:d} requer {xp_requerido:d} de XP acumulado')
def step_define_requisito_xp(context, nivel, xp_requerido):
    inicializa_contexto(context)
    xp_do_modelo = manager.pegar_xp_nivel(nivel)
    assert xp_do_modelo == xp_requerido, (
        f"Para o nível {nivel}, o XP esperado era {xp_requerido}, "
        f"mas o modelo tem {xp_do_modelo} de XP."
    )
    context.xp_por_nivel[nivel] = xp_requerido


@when('o personagem "{nome}" tenta subir de nível')
def step_tenta_subir_de_nivel(context, nome):
    inicializa_contexto(context)
    personagem = context.personagens[nome]
    manager.tentar_subir_de_nivel(personagem, context.xp_por_nivel)


@then('o personagem "{nome}" deve estar no nível {nivel_esperado:d}')
def step_verifica_nivel(context, nome, nivel_esperado):
    inicializa_contexto(context)
    personagem = context.personagens[nome]
    assert personagem['nivel'] == nivel_esperado, (
        f"Esperava que o personagem '{nome}' estivesse no nível {nivel_esperado}, "
        f"mas ele está no nível {personagem['nivel']} com {personagem['xp_acumulado']} XP."
    )


@then('o personagem "{nome}" deve continuar no nível {nivel_esperado:d}')
def step_deve_continuar_no_nivel(context, nome, nivel_esperado):
    step_verifica_nivel(context, nome, nivel_esperado)

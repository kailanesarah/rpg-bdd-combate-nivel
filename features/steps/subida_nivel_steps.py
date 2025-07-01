from behave import given, when, then

# Dados dos níveis e XP
niveis_data = [
    {"nivel": 1, "xp": 0},
    {"nivel": 2, "xp": 10},
    {"nivel": 3, "xp": 100},
    {"nivel": 4, "xp": 200},
    {"nivel": 5, "xp": 300},
    {"nivel": 6, "xp": 500},
]

# Função auxiliar para pegar o XP necessário para determinado nível
def pegar_xp_nivel(nivel_personagem):
    for nivel_info in niveis_data:
        if nivel_info['nivel'] == nivel_personagem:
            return nivel_info['xp']
    return None

# Função auxiliar para inicializar o contexto
def inicializa_contexto(context):
    if not hasattr(context, 'xp_por_nivel'):
        context.xp_por_nivel = {item['nivel']: item['xp']
                                for item in niveis_data}
    if not hasattr(context, 'personagens'):
        context.personagens = {}


@given('que o personagem "{nome}" está no nível {nivel:d}')
def step_cria_personagem(context, nome, nivel):
    inicializa_contexto(context)
    context.personagens[nome] = {
        'nome': nome,
        'nivel': nivel,
        'xp_acumulado': 0
    }


@given('o personagem "{nome}" possui {xp:d} de XP acumulado')
def step_define_xp(context, nome, xp):
    inicializa_contexto(context)
    if nome not in context.personagens:
        raise ValueError(f"O personagem '{nome}' não foi criado.")
    context.personagens[nome]['xp_acumulado'] = xp


@given('o nível {nivel:d} requer {xp_requerido:d} de XP acumulado')
def step_define_requisito_xp(context, nivel, xp_requerido):
    inicializa_contexto(context)
    xp_do_modelo = pegar_xp_nivel(nivel)
    assert xp_do_modelo == xp_requerido, (
        f"Para o nível {nivel}, o XP esperado era {xp_requerido}, "
        f"mas o modelo tem {xp_do_modelo} de XP."
    )
    context.xp_por_nivel[nivel] = xp_requerido


@when('o personagem "{nome}" tenta subir de nível')
def step_tenta_subir_de_nivel(context, nome):
    inicializa_contexto(context)
    personagem = context.personagens[nome]
    xp_acumulado = personagem['xp_acumulado']
    nivel_atual = personagem['nivel']

    sorteia_nivel = sorted(context.xp_por_nivel.items())

    novo_nivel = nivel_atual
    for nivel, xp_necessario in sorteia_nivel:
        if xp_acumulado >= xp_necessario and nivel > novo_nivel:
            novo_nivel = nivel

    personagem['nivel'] = novo_nivel


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

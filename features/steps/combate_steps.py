from behave import given, when, then
from src.personagem import Personagem
from src.combate import atacar

# História 1: Ataque reduz vida

@given('um personagem "{nome}" com {vida:d} de vida')
def step_personagem(context, nome, vida):
    context.atacante = Personagem(nome, vida)

@given('um inimigo "{nome}" com {vida:d} de vida')
def step_inimigo(context, nome, vida):
    context.defensor = Personagem(nome, vida)

@given('uma arma "{nome}" com dano {dano:d}')
def step_arma(context, nome, dano):
    context.arma = {"nome": nome, "dano": dano}

@when('"{atacante}" ataca "{defensor}" com "{arma}"')
def step_ataque(context, atacante, defensor, arma):
    context.ataque_realizado = atacar(context.atacante, context.defensor, context.arma)

@then('a vida do "{nome}" deve ser {vida:d}')
def step_verifica_vida(context, nome, vida):
    assert context.defensor.vida == vida

# História 2: Inimigo pode ser derrotado

@given('a vida do "{nome}" é {vida:d}')
def step_set_vida(context, nome, vida):
    context.defensor.vida = vida
    context.defensor.derrotado = (vida == 0)

@then('"{nome}" está derrotado')
def step_verifica_derrotado(context, nome):
    assert context.defensor.derrotado is True

# História 3: Não é possível atacar inimigo derrotado

@when('"{atacante}" tenta atacar "{defensor}" com "{arma}"')
def step_tenta_ataque(context, atacante, defensor, arma):
    context.ataque_realizado = atacar(context.atacante, context.defensor, context.arma)

@then('o ataque é ignorado')
def step_ataque_ignorado(context):
    assert context.ataque_realizado is False

def atacar(atacante, defensor, arma):
    if defensor.derrotado:
        return False 

    defensor.receber_dano(arma["dano"])
    return True

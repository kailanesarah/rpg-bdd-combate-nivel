Feature: Subida de nível por acúmulo de XP
    Como jogador
    Quero que meu personagem suba de nível conforme a experiência que adquiriu
    Para que ele possa evoluir e ficar mais forte

    # Tabela com níveis e seus respectivos XPs necessários para subida:
    # | Nível alcançado | XP total necessário |
    # | Nível 01         | 0                   |
    # | Nível 02         | 10                  |
    # | Nível 03         | 100                 |
    # | Nível 04         | 200                 |
    # | Nível 05         | 300                 |
    # | Nível 06         | 500                 |

    Scenario: Personagem avança de nível ao acumular XP suficiente
        Given que o personagem "Nécio" está no nível 2
        And o personagem "Nécio" possui 24 de XP acumulado
        And o nível 3 requer 100 de XP acumulado
        When o personagem "Nécio" tenta subir de nível
        Then o personagem "Nécio" deve continuar no nível 2

    Scenario: Personagem não sobe de nível quando o XP acumulado for insuficiente
        Given que o personagem "Sarah" está no nível 2
        And o personagem "Sarah" possui 51 de XP acumulado
        And o nível 3 requer 100 de XP acumulado
        When o personagem "Sarah" tenta subir de nível
        Then o personagem "Sarah" deve continuar no nível 2


 
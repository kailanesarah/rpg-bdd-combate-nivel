Feature: Subida de nível por acumulo de XP
    Como jogador
    Quero que meu personagem suba de nível conforme a experiência que adquiriu
    Para que ele possa evoluir e ficar mais forte

    #Tabela com níveis e seus respectivos XPs
    #|Nível alcançado|--------------------|XP Total necessário|
    #|Nível 01       |--------------------|0                  |
    #|Nível 02       |--------------------|10                 |
    #|Nível 03       |--------------------|100                |
    #|Nível 04       |--------------------|200                |
    #|Nível 05       |--------------------|300                |
    #|Nível 06       |--------------------|500                |

    #Os cenários devem focar em situações onde o XP acumulado do personagem atinge ou ultrapassa o limiar para o próximo nível.

    Scenario: Personagem avança do Nível 1 para o Nível 2 ao acumular XP
        Given que o personagem "Nécio" está no nível 01
        And ele possui 0 de XP acumulado
        And o nível 02 requer 10 de XP acumulado
        When ele completa a missão "Derrote 3 bandidos" (que concede 10 de XP)
        Then "Nécio" deve estar com 10 de XP acumulado
        And deve subir para o nível 02

    Scenario: Personagem não sobe de nível quando o XP acumulado for insuficiente
        Given que o personagem "Natália" 40 de XP acumulado
        And o nível 03 requer 100 de XP acumulado 
        When "Natália" completa a missão "Recupere a pedra mágica" (concede 20 de XP)
        And também completa a missão "Ajude a idosa a encontrar seu gato " (concede 14 de XP)
        Then "Natália" deve ter agora 74 de XP acumulado
        And deve permanecer no nível 02

    Scenario: Personagem realiza missões e passa vários níveis de uma vez
        Given que o personagem "Alex" possui 74 de XP acumulado
        And os próximos níveis 03 e 04 precisam no mímimo de 300 de XP acumulado
        When "Alex" completa a missão "Salve a princesa do castelo inimigo" (que concede 150 de XP)
        And também completa a missão "Mate o dragão" (concede 200 de XP)
        Then "Alex" deve ter agora 424 de XP acumulado
        And deve subir para o nível 05

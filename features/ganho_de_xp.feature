Feature: Ganhar experiência (XP)
    Como jogador
    Quero que meu personagem ganhe experiência ao realizar missões
    Para que ele possa evoluir e subir de nível

    Background: Tabela de XP por tipo de missão
        | Nome da Missão                            | Tipo              | XP Ganho |
        | Derrote 3 bandidos                        | Matar inimigos    | 10       |
        | Recupere a pedra mágica                   | Coletar itens     | 20       |
        | Entregue comida a um sem-teto             | Ajudar pessoas    | 12       |
        | Elimine o chefe dos bandidos              | Matar inimigos    | 18       |
        | Ajude a idosa a encontrar seu gato        | Ajudar pessoas    | 14       |

    Scenario: Personagem em nível inicial quer ganhar XP
        Given que o personagem "Nécio" está no nível 1 e possui 10 de XP
        And a missão "Ajude a idosa a encontrar seu gato" garante 14 de XP
        When "Nécio" completa a missão "Ajude a idosa a encontrar seu gato"
        Then ele deve ter 34 de XP

    Scenario: Personagem recupera um item mágico
        Given que a personagem "Sarah" está no nível 2 com 31 de XP
        And a missão "Recupere a pedra mágica" garante 20 de XP
        When "Sarah" completa a missão "Recupere a pedra mágica"
        Then ela deve ter 51 de XP

    Scenario: Personagem elimina o chefe dos bandidos
        Given que o personagem "Diego" está no nível 5 com 180 de XP
        And a missão "Elimine o chefe dos bandidos" garante 18 de XP
        When "Diego" completa a missão "Elimine o chefe dos bandidos"
        Then ele deve ter 198 de XP

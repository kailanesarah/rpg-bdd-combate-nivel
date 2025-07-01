Feature: Ganhar experiência (XP)
    Como jogador
    Quero que meu personagem ganhe experiência ao realizar missões
    Para que ele possa evoluir e subir de nível

        #Tabela de XP por tipo de missão
        #| Nome da Missão                            | Tipo              | XP Ganho |
        #| Derrote 3 bandidos                        | Matar inimigos    | 10       |
        #| Recupere a pedra mágica                   | Coletar itens     | 20       |
        #| Entregue comida a um sem-teto             | Ajudar pessoas    | 12       |
        #| Elimine o chefe dos bandidos              | Matar inimigos    | 18       |
        #| Ajude a idosa a encontrar seu gato        | Ajudar pessoas    | 14       |
        #| Salve a princesa do castelo inimigo       | Ajudar pessoas    | 150      |
        #| Mate o dragão                             | Ajudar pessoas    | 200      |
        #| Roube o ouro do dragão                    | Ajudar pessoas    | 70       |

    Scenario: Personagem em nível inicial quer ganhar XP
        Given que o personagem "Nécio" está no Nível 1
        And "Nécio" possui 10 de XP acumulado
        And a missão "Ajude a idosa a encontrar seu gato" garante 14 de XP
        When personagem "Nécio" completa a missão "Ajude a idosa a encontrar seu gato"
        Then ele deve ter 24 de XP

    Scenario: Personagem recupera um item mágico
        Given que o personagem "Sarah" está no Nível 2
        And "Sarah" possui 31 de XP acumulado
        And a missão "Recupere a pedra mágica" garante 20 de XP
        When personagem "Sarah" completa a missão "Recupere a pedra mágica"
        Then ele deve ter 51 de XP

    Scenario: Personagem elimina o chefe dos bandidos
        Given que o personagem "Alex" está no Nível 4
        And "Alex" possui 180 de XP acumulado
        And a missão "Elimine o chefe dos bandidos" garante 18 de XP
        When personagem "Alex" completa a missão "Elimine o chefe dos bandidos"
        Then ele deve ter 198 de XP

Feature: Sistema de Combate de RPG

  Background:
    Given um personagem "Arqueiro" com 100 de vida
    And um inimigo "Goblin" com 30 de vida
    And uma arma "Arco Curto" com dano 15

  Scenario: Ataque reduz a vida do inimigo
    When "Arqueiro" ataca "Goblin" com "Arco Curto"
    Then a vida do "Goblin" deve ser 15

  Scenario: Ataque que derrota o inimigo
    Given a vida do "Goblin" é 10
    When "Arqueiro" ataca "Goblin" com "Arco Curto"
    Then "Goblin" está derrotado

  Scenario: Não é possível atacar um inimigo já derrotado
    Given a vida do "Goblin" é 0
    When "Arqueiro" tenta atacar "Goblin" com "Arco Curto"
    Then o ataque é ignorado
    And a vida do "Goblin" deve ser 0

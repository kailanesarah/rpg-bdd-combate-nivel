# RPG BDD – Combate e Subida de Nível

## 🎯 Domínio do Projeto

Jogo de RPG com foco em duas funcionalidades principais:

- **Combate** (ataque, dano, vida)
- **Subida de nível** (ganho de experiência, evolução de nível)

---

## 🧑‍🤝‍🧑 Divisão Direta de Tarefas

### Alex Magalhães – Responsável principal por **Combate**

- Escrever 3 histórias BDD no arquivo `combate.feature`
- Criar o código da funcionalidade de combate (`src/combate.py`)
- Implementar os step definitions em `steps/combate_steps.py`
- Gerar e rodar testes automáticos para validar o combate
- Tirar prints dos testes funcionando para o PDF final
- Criar a seção **Combate** no PDF, incluindo histórias, código e resultados

---

### Kailane Sarah – Responsável principal por **Subida de Nível** e **Ganho de XP**

- Escrever 3 histórias BDD no arquivo `subida_de_nivel.feature`
- Escrever 3 histórias BDD no arquivo `ganho_de_xp.feature`
- Criar o código da funcionalidade de subida de nível (`src/nivel.py`)
- Implementar os step definitions em `steps/subida_nivel_steps.py`
- Gerar e rodar testes automáticos para validar a evolução de nível
- Tirar prints dos testes funcionando para o PDF final
- Criar a seção **Subida de Nível** no PDF, incluindo histórias, código e resultados

---

### 🤝 Tarefas colaborativas (ambos juntos)

| Tarefa                                   | Responsável              |
|-----------------------------------------|---------------------------|
| Escolher regras do jogo (vida, XP, níveis, etc.) | Ambos            |
| Revisar os arquivos `.feature` um do outro       | Ambos            |
| Criar e configurar o repositório no GitHub       | Ambos            |
| Criar o PDF final com capa, sumário e links      | Ambos            |
| Preencher o README.md com descrição do projeto   | Ambos            |


## ⚙️ Ambiente de Desenvolvimento

Para garantir que todas as dependências estejam instaladas corretamente, siga os passos abaixo para criar e ativar um ambiente virtual (venv) e instalar os pacotes necessários.


### Criar e ativar a venv

No terminal, dentro da pasta raiz do projeto:

```bash
python3 -m venv venv
```

Para ativar no Linux/Mac:

```bash
source venv/bin/activate
```

Para ativar no Windows:

```bash
venv\Scripts\activate
```

Instalar dependências
Com a venv ativada, execute:

```bash
pip install -r requirements.txt
```

---
## 🎯 Objetivos finais

- Implementar as funcionalidades seguindo as histórias BDD.
- Gerar testes automatizados para garantir que o sistema funciona conforme esperado.
- Documentar todo o processo, incluindo histórias, código e resultados dos testes, em um arquivo PDF.
- Manter o código versionado e colaborativo via GitHub, com commits de todos os membros da equipe.

---
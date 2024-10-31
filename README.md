# Jogo da Memória - Projeto Universitário

## Descrição

Este projeto é um jogo da memória desenvolvido para o curso de **Programação Funcional**. É um jogo simples onde os jogadores viram cartas para encontrar pares correspondentes. O jogo é construído usando Python e Pygame, aderindo a conceitos de programação funcional sempre que possível. Ele aplica conceitos fundamentais como imutabilidade, funções puras e código declarativo para criar uma experiência de jogo envolvente. O projeto demonstra os princípios da programação funcional na prática, reforçando seu uso por meio de uma aplicação interativa.

## Pré-requisitos

- **Python 3.6** ou superior
- **pip** (gerenciador de pacotes)
- Biblioteca **Pygame** (instalada via `requirements.txt`)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/giovannivicentin/memory-game-university-project.git
   cd memory-game-university-project
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**

- No Windows:

  ```bash
  venv\Scripts\activate
  ```

- No macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

4. **Instale as dependências necessárias:**

   ```bash
   pip install -r requirements.txt
   ```

## Como Utilizar

Execute o jogo com o seguinte comando:

```bash
python src/main.py
```

## Estrutura do Projeto

```bash
memory-game-university-project/
├── README.md
├── requirements.txt
├── .gitignore
├── images/
│ ├── card_0.png
│ ├── card_1.png
│ ├── card_2.png
│ ├── card_3.png
│ ├── card_4.png
│ ├── card_5.png
│ ├── card_6.png
│ ├── card_7.png
│ └── back.png
├── src/
│ ├── __init__.py
│ ├── main.py
│ ├── game_logic.py
│ └── ui.py
└── tests/
├── __init__.py
└── test_game_logic.py
```

#### Explicação da estrutura:

- src/: Contém todo o código-fonte.

- main.py: O ponto de entrada da aplicação.

- game_logic.py: Implementa a lógica central do jogo utilizando princípios de programação funcional.

- ui.py: Gerencia os componentes da interface do usuário com Pygame.

- tests/: Contém testes unitários para a lógica do jogo.

- images/: Contém todas as imagens utilizadas para compor o jogo.

## Funcionalidades

- Jogabilidade Simples: Clique nas cartas para virá-las e encontrar pares correspondentes.

- Princípios de Programação Funcional: Enfatiza funções puras, imutabilidade e código declarativo.

- Interface Gráfica: Construída com Pygame para uma experiência interativa.

- Testes Unitários: Inclui testes para garantir a correção da lógica do jogo.

## Princípios de Programação Funcional Aplicados

- Funções Puras: As funções de lógica do jogo são puras, retornando novos estados do jogo sem efeitos colaterais.

- Imutabilidade: Utiliza estruturas de dados imutáveis; o estado do jogo não é modificado, mas substituído por novas instâncias.

- Funções de Primeira Classe: Funções são passadas como argumentos para outras funções, promovendo funções de ordem superior.

- Código Declarativo: Foca no que o programa deve realizar, em vez de como realizá-lo.

## Testes

Execute os testes unitários com:

```bash
python -m unittest discover tests
```

## Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do repositório para sua própria conta do GitHub.

2. Crie um novo branch para sua funcionalidade ou correção de bug:

   ```bash
   git checkout -b feature/sua-funcionalidade
   ```

3. Comite suas alterações com mensagens claras:

   ```bash
   git commit -m "Adicionar funcionalidade: sua funcionalidade"
   ```

4. Faça push para seu fork:
   ```bash
   git push origin feature/sua-funcionalidade
   ```

5. Crie um pull request no repositório original.

## Licença

Este projeto está licenciado sob a Licença MIT.

## Agradecimentos

- Curso Universitário: Desenvolvido como um projeto para o curso de Programação Funcional.

- Pygame: Usado para criar a interface gráfica do usuário.

- Comunidade Open-Source: Agradecimentos a todos os colaboradores open-source por seus recursos inestimáveis.

Sinta-se à vontade para explorar o código, jogar o jogo e contribuir para o projeto!

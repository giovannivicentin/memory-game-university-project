# Memory Game University Project

## Description

This project is a memory game developed for the **Functional Programming** course. It's a simple game where players flip over cards to find matching pairs. The game is built using Python and Pygame, adhering to functional programming concepts where possible. It applies core concepts like immutability, pure functions, and declarative code to create an engaging game experience. The project demonstrates functional programming principles in practice, reinforcing their usage through an interactive application.

## Prerequisites

- **Python 3.6** or higher
- **pip** package manager
- **Pygame** library (installed via `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/giovannivicentin/memory-game-university-project.git
   cd memory-game-university-project
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the game using the following command:

```bash
python src/main.py
```

## Project Structure

```bash
memory-game-university-project/<br>
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│ ├── __init__.py
│ ├── main.py
│ ├── game_logic.py
│ └── ui.py
└── tests/
├── __init__.py
└── test_game_logic.py
```

#### Explanation of structure:

- src/: Contains all the source code.

- main.py: The entry point of the application.

- game_logic.py: Implements the core game logic using
  functional programming principles.

- ui.py: Manages the user interface components with Pygame.

- tests/: Contains unit tests for the game logic.

## Features

- Simple Gameplay: Click on cards to flip them and find matching pairs.

- Functional Programming Principles: Emphasizes pure functions, immutability, and declarative code.

- Graphical User Interface: Built with Pygame for an interactive experience.

- Unit Testing: Includes tests to ensure the correctness of the game logic.

## Functional Programming Principles Applied

- Pure Functions: Game logic functions are pure, returning new game states without side effects.

- Immutability: Uses immutable data structures; the game state is not modified but replaced with new instances.

- First-Class Functions: Functions are passed as arguments to other functions, promoting higher-order functions.

- Declarative Code: Focuses on what the program should accomplish rather than how to accomplish it.

## Testing

Run the unit tests with:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository to your own GitHub account.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes with clear messages:

   ```bash
   git commit -m "Add feature: your feature name"
   ```

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request in the original repository.

## License

This project is licensed under the MIT License.

## Acknowledgments

- University Course: Developed as a project for the Functional Programming course.

- Pygame: Used for creating the graphical user interface.

- Open-Source Community: Thanks to all open-source contributors for their invaluable resources.

Feel free to explore the code, play the game, and contribute to the project!

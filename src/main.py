from game_logic import initialize_game, update_game_state
from ui import run_game_loop


def main():
    game_state = initialize_game()
    run_game_loop(game_state, update_game_state)


if __name__ == "__main__":
    main()

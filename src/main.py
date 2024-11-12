from game_logic import initialize_game, update_game_state
from ui import run_start_screen, run_game_loop


def main():
    action = run_start_screen()

    if action == "play":
        game_state = initialize_game()
        run_game_loop(game_state, update_game_state)


if __name__ == "__main__":
    main()

from game_logic import initialize_game, flip_card, check_for_match
from ui import display_game, get_player_input


def main():
    game_state = initialize_game()
    while not game_state["game_over"]:
        display_game(game_state)
        position = get_player_input()
        game_state = flip_card(game_state, position)
        game_state = check_for_match(game_state)
    print("Congratulations! You've completed the game.")


if __name__ == "__main__":
    main()

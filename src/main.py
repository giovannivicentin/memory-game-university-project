from game_logic import initialize_game, update_game_state
from ui import run_start_screen, run_game_loop


def main():
    # Display the start screen and wait for the player's action
    action = run_start_screen()

    if action == "play":
        game_state = initialize_game()
        
        while True:
            result = run_game_loop(game_state, update_game_state)

            if result == "exit":
                pygame.quit()  # Exit the game if the player chooses "Exit"
                break
            elif result == "restart":
                game_state = initialize_game()  # Reset the game state if "Restart" is clicked
                continue  # Start a new game loop

if __name__ == "__main__":
    main()

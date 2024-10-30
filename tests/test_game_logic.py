import unittest
from src.game_logic import initialize_game, flip_card, check_for_match


class TestGameLogic(unittest.TestCase):

    def test_initialize_game(self):
        game_state = initialize_game()
        self.assertIsInstance(game_state, dict)
        self.assertEqual(len(game_state["deck"]), 16)
        self.assertIsNone(game_state["first_selection"])
        self.assertIsNone(game_state["second_selection"])
        self.assertFalse(game_state["game_over"])

    def test_flip_card(self):
        game_state = initialize_game()
        index = 0
        new_state = flip_card(game_state, index)
        self.assertNotEqual(game_state, new_state)
        self.assertTrue(new_state["deck"][index].flipped)
        self.assertEqual(new_state["first_selection"], index)

    def test_check_for_match(self):
        game_state = initialize_game()
        index1 = 0
        index2 = 1
        # Flip first card
        game_state = flip_card(game_state, index1)
        # Flip second card
        game_state = flip_card(game_state, index2)
        # Check for match
        game_state = check_for_match(game_state)
        self.assertIsNone(game_state["first_selection"])
        self.assertIsNone(game_state["second_selection"])
        self.assertFalse(game_state["waiting"])
        card1 = game_state["deck"][index1]
        card2 = game_state["deck"][index2]
        if card1.id == card2.id:
            self.assertTrue(card1.matched)
            self.assertTrue(card2.matched)
        else:
            self.assertFalse(card1.flipped)
            self.assertFalse(card2.flipped)


if __name__ == "__main__":
    unittest.main()

import random
from collections import namedtuple

# Define a Card namedtuple
Card = namedtuple("Card", ["id", "flipped", "matched"])


def create_deck():

    # Creates a shuffled deck of cards and returns a list of Card namedtuples.
    num_pairs = 8  # For a 4x4 grid
    card_ids = list(range(num_pairs)) * 2  # Create pairs
    random.shuffle(card_ids)
    deck = [Card(id=card_id, flipped=False, matched=False) for card_id in card_ids]
    return deck


def initialize_game():

    # Initializes the game state and returns a dictionary representing the game state.

    deck = create_deck()
    game_state = {
        "deck": deck,
        "first_selection": None,
        "second_selection": None,
        "waiting": False,
        "matches_found": 0,
        "game_over": False,
    }
    return game_state


def flip_card(game_state, index):

    # Flips a card at the given index and returns a new game state.

    deck = game_state["deck"]
    card = deck[index]

    if card.flipped or card.matched or game_state["waiting"]:
        return game_state

    # flip here
    new_card = Card(id=card.id, flipped=True, matched=card.matched)
    new_deck = deck[:index] + [new_card] + deck[index + 1 :]

    if game_state["first_selection"] is None:
        new_game_state = game_state.copy()
        new_game_state["deck"] = new_deck
        new_game_state["first_selection"] = index
        return new_game_state
    else:
        new_game_state = game_state.copy()
        new_game_state["deck"] = new_deck
        new_game_state["second_selection"] = index
        new_game_state["waiting"] = True
        return new_game_state


def check_for_match(game_state):

    # Checks if the two selected cards are a match. return a new game state.
    first_index = game_state["first_selection"]
    second_index = game_state["second_selection"]

    if first_index is None or second_index is None:
        return game_state

    deck = game_state["deck"]
    first_card = deck[first_index]
    second_card = deck[second_index]

    new_deck = deck[:]

    if first_card.id == second_card.id:
        # It's a match
        new_first_card = Card(id=first_card.id, flipped=True, matched=True)
        new_second_card = Card(id=second_card.id, flipped=True, matched=True)
        new_deck[first_index] = new_first_card
        new_deck[second_index] = new_second_card

        matches_found = game_state["matches_found"] + 1
    else:
        new_first_card = Card(id=first_card.id, flipped=False, matched=False)
        new_second_card = Card(id=second_card.id, flipped=False, matched=False)
        new_deck[first_index] = new_first_card
        new_deck[second_index] = new_second_card
        matches_found = game_state["matches_found"]

    new_game_over = matches_found == len(deck) // 2

    new_game_state = {
        "deck": new_deck,
        "first_selection": None,
        "second_selection": None,
        "waiting": False,
        "matches_found": matches_found,
        "game_over": new_game_over,
    }
    return new_game_state


def update_game_state(game_state, action):

    # Updates the game state based on an action and return a new game state
    if action["type"] == "flip_card":
        index = action["index"]
        game_state = flip_card(game_state, index)
    elif action["type"] == "check_match":
        game_state = check_for_match(game_state)
    return game_state

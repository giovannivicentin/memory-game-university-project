import os
import pygame

pygame.font.init()

CARD_SIZE = (100, 100)
MARGIN = 10
ROWS = 4
COLS = 4
SCREEN_SIZE = (
    COLS * (CARD_SIZE[0] + MARGIN) + MARGIN,
    ROWS * (CARD_SIZE[1] + MARGIN) + MARGIN,
)

FONT = pygame.font.SysFont("Arial", 24)


# this function make the images rounded in borders
def create_rounded_image(image, radius):
    rect = image.get_rect()
    mask = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(mask, (255, 255, 255, 255), mask.get_rect(), border_radius=radius)
    rounded_image = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    rounded_image.blit(image, (0, 0))
    rounded_image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    return rounded_image


def load_card_images():
    images = {}
    for i in range(8):
        image_path = os.path.join("images", f"card_{i}.png")
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, CARD_SIZE)
        image = create_rounded_image(image, radius=15)
        images[i] = image
    return images


def load_back_image():
    image_path = os.path.join("images", "back.png")
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Back image file not found: {image_path}")
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, CARD_SIZE)
    image = create_rounded_image(image, radius=15)
    return image


def draw_game(screen, game_state, card_images, back_image):
    # this is the rgb of background
    screen.fill((000, 000, 000))
    deck = game_state["deck"]
    for index, card in enumerate(deck):
        row = index // COLS
        col = index % COLS
        x = MARGIN + col * (CARD_SIZE[0] + MARGIN)
        y = MARGIN + row * (CARD_SIZE[1] + MARGIN)

        if card.flipped or card.matched:
            image = card_images[card.id]
        else:
            image = back_image
        screen.blit(image, (x, y))
    pygame.display.flip()


def get_card_index(pos):
    x, y = pos
    for index in range(ROWS * COLS):
        row = index // COLS
        col = index % COLS
        card_x = MARGIN + col * (CARD_SIZE[0] + MARGIN)
        card_y = MARGIN + row * (CARD_SIZE[1] + MARGIN)
        rect = pygame.Rect(card_x, card_y, CARD_SIZE[0], CARD_SIZE[1])
        if rect.collidepoint(x, y):
            return index
    return None


def display_game_over(screen):

    text_surface = FONT.render(
        "Congratulations! You've completed the game.", True, (0, 0, 0)
    )
    screen.blit(
        text_surface,
        (
            SCREEN_SIZE[0] // 2 - text_surface.get_width() // 2,
            SCREEN_SIZE[1] // 2 - text_surface.get_height() // 2,
        ),
    )
    pygame.display.flip()


def run_game_loop(game_state, update_game_state):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Memory Game")

    card_images = load_card_images()
    back_image = load_back_image()

    clock = pygame.time.Clock()
    running = True
    timer = 0
    delay = 1000

    while running:
        if game_state["game_over"]:
            display_game_over(screen)
            pygame.time.wait(3000)
            running = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_state["waiting"]:
                pos = pygame.mouse.get_pos()
                index = get_card_index(pos)
                if index is not None:
                    action = {"type": "flip_card", "index": index}
                    game_state = update_game_state(game_state, action)
                    if game_state["waiting"]:
                        timer = pygame.time.get_ticks()
            elif game_state["waiting"]:
                current_time = pygame.time.get_ticks()
                if current_time - timer >= delay:
                    action = {"type": "check_match"}
                    game_state = update_game_state(game_state, action)

        draw_game(screen, game_state, card_images, back_image)
        clock.tick(30)

    pygame.quit()

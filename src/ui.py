import os
import pygame

pygame.font.init()

CARD_SIZE = (150, 150)
MARGIN = 10
ROWS = 4
COLS = 4
SCREEN_SIZE = (
    COLS * (CARD_SIZE[0] + MARGIN) + MARGIN,
    ROWS * (CARD_SIZE[1] + MARGIN) + MARGIN,
)

FONT = pygame.font.SysFont("Arial", 24)


# This function makes the images have rounded borders
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
        image = pygame.transform.smoothscale(image, CARD_SIZE)
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


def draw_game(
    screen, game_state, card_images, back_image, animations, animation_duration
):
    # This is the RGB color of the background
    screen.fill((0, 0, 0))
    deck = game_state["deck"]
    for index, card in enumerate(deck):
        row = index // COLS
        col = index % COLS
        x = MARGIN + col * (CARD_SIZE[0] + MARGIN)
        y = MARGIN + row * (CARD_SIZE[1] + MARGIN)

        if index in animations:
            animation = animations[index]
            progress = animation["progress"] / animation_duration
            if progress < 0.5:
                # First half of animation, shrinking
                scale = 1 - (progress * 2)
                image = back_image
            else:
                # Second half, expanding
                scale = (progress - 0.5) * 2
                image = card_images[card.id]
            scaled_width = int(CARD_SIZE[0] * abs(scale))
            if scaled_width > 0:
                scaled_image = pygame.transform.scale(
                    image, (scaled_width, CARD_SIZE[1])
                )
                image_x = x + (CARD_SIZE[0] - scaled_width) // 2
                screen.blit(scaled_image, (image_x, y))
        else:
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
        "Congratulations! You've completed the game.", True, (255, 255, 255)
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

    animations = {}
    animation_duration = 280

    while running:
        dt = clock.tick(30)

        if game_state["game_over"]:
            display_game_over(screen)
            pygame.time.wait(3000)
            running = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and not game_state["waiting"]
                and len(animations) == 0
            ):
                pos = pygame.mouse.get_pos()
                index = get_card_index(pos)
                if index is not None:
                    card = game_state["deck"][index]
                    if not card.flipped and not card.matched:
                        animations[index] = {"progress": 0.0, "flipped": False}

        for index in list(animations.keys()):
            animation = animations[index]
            animation["progress"] += dt
            normalized_progress = animation["progress"] / animation_duration

            if not animation["flipped"] and normalized_progress >= 0.5:
                action = {"type": "flip_card", "index": index}
                game_state = update_game_state(game_state, action)
                animation["flipped"] = True
                if game_state["waiting"]:
                    timer = pygame.time.get_ticks()

            if normalized_progress >= 1.0:
                del animations[index]

        if game_state["waiting"] and len(animations) == 0:
            current_time = pygame.time.get_ticks()
            if current_time - timer >= delay:
                action = {"type": "check_match"}
                game_state = update_game_state(game_state, action)

        draw_game(
            screen,
            game_state,
            card_images,
            back_image,
            animations,
            animation_duration,
        )

    pygame.quit()

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
BIG_FONT = pygame.font.SysFont("Arial", 48)

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

def draw_start_screen(screen):
    # Background color
    screen.fill((30, 30, 30))

    # Title
    title_text = BIG_FONT.render("Amadeu's Memories", True, (255, 255, 255))
    screen.blit(
        title_text,
        (
            SCREEN_SIZE[0] // 2 - title_text.get_width() // 2,
            SCREEN_SIZE[1] // 4 - title_text.get_height() // 2,
        ),
    )

    # Play Button
    play_button_rect = pygame.Rect(
        SCREEN_SIZE[0] // 2 - 100, SCREEN_SIZE[1] // 2, 200, 50
    )
    pygame.draw.rect(screen, (100, 200, 100), play_button_rect, border_radius=10)
    play_text = FONT.render("Play", True, (255, 255, 255))
    screen.blit(
        play_text,
        (
            play_button_rect.centerx - play_text.get_width() // 2,
            play_button_rect.centery - play_text.get_height() // 2,
        ),
    )

    # Info Button
    info_button_rect = pygame.Rect(SCREEN_SIZE[0] - 50, 10, 40, 40)
    pygame.draw.circle(screen, (255, 255, 255), info_button_rect.center, 20)
    info_text = FONT.render("i", True, (0, 0, 0))
    screen.blit(
        info_text,
        (
            info_button_rect.centerx - info_text.get_width() // 2,
            info_button_rect.centery - info_text.get_height() // 2,
        ),
    )

    pygame.display.flip()

    return play_button_rect, info_button_rect


def draw_info_screen(screen, game_state):
    # Cor de fundo semitransparente para a tela de informações

    overlay_color = (0, 0, 0, 200)  # Preto com transparência
    overlay = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)  # Surface com canal alfa
    overlay.fill(overlay_color)  # Preenche com a cor de transparência

    # Desenha o fundo translúcido
    screen.blit(overlay, (0, 0))

    info_text = [
        "",
        "Autores:",
        "Giovanni Vicentin",
        "Felipe Destro",
        "Gabriel Araujo",
        "Paulo Sérgio",
        "",
        "Clique em qualquer lugar para sair desta tela."
    ]

    # Renderiza cada linha do texto
    y_offset = SCREEN_SIZE[1] // 4  # Começa a desenhar um pouco abaixo do topo
    for line in info_text:
        text_surface = FONT.render(line, True, (255, 255, 255))
        screen.blit(
            text_surface,
            (SCREEN_SIZE[0] // 2 - text_surface.get_width() // 2, y_offset)
        )
        y_offset += text_surface.get_height() + 10  # Ajuste do espaçamento entre as linhas

    pygame.display.flip()


def get_button_index(pos, play_button_rect, info_button_rect):
    if play_button_rect.collidepoint(pos):
        return "play"
    elif info_button_rect.collidepoint(pos):
        return "info"
    return None


def run_start_screen():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Amadeu's Memories")

    play_button_rect, info_button_rect = draw_start_screen(screen)
    running = True
    info_shown = False

    # Criando um 'game_state' fictício para a tela de informações
    game_state = {}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                button_clicked = get_button_index(pos, play_button_rect, info_button_rect)
                if button_clicked == "play":
                    return "play"
                elif button_clicked == "info" and not info_shown:
                    info_shown = True
                    draw_info_screen(screen, game_state)
                elif info_shown:
                    info_shown = False
                    draw_start_screen(screen)

    pygame.quit()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                button_clicked = get_button_index(pos, play_button_rect, info_button_rect)
                if button_clicked == "play":
                    return "play"
                elif button_clicked == "info" and not info_shown:
                    info_shown = True
                    draw_info_screen(screen)
                elif info_shown:
                    info_shown = False
                    draw_start_screen(screen)

    pygame.quit()

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


def draw_game_over_screen(screen):
    # Carregar a imagem de fundo
    fundo = pygame.image.load("images/fundosaida.jpeg")
    fundo = pygame.transform.scale(fundo, SCREEN_SIZE)  # Ajustar à resolução da tela
    screen.blit(fundo, (0, 0))  # Desenhar a imagem no fundo

    # Texto "Parabéns Você Ganhou"
    game_over_text = BIG_FONT.render("Parabéns Você Ganhou(:", True, (0, 0, 0))  # Cor preta
    screen.blit(
        game_over_text,
        (
            SCREEN_SIZE[0] // 2 - game_over_text.get_width() // 2,
            SCREEN_SIZE[1] // 4 - game_over_text.get_height() // 2,
        ),
    )

    # Botão "Jogar Novamente"
    restart_button_rect = pygame.Rect(
        SCREEN_SIZE[0] // 2 - 100, SCREEN_SIZE[1] // 2, 200, 50
    )
    pygame.draw.rect(screen, (100, 200, 100), restart_button_rect, border_radius=10)
    restart_text = FONT.render("Jogar Novamente", True, (255, 255, 255))
    screen.blit(
        restart_text,
        (
            restart_button_rect.centerx - restart_text.get_width() // 2,
            restart_button_rect.centery - restart_text.get_height() // 2,
        ),
    )

    # Botão "Sair"
    exit_button_rect = pygame.Rect(
        SCREEN_SIZE[0] // 2 - 100, SCREEN_SIZE[1] // 2 + 60, 200, 50
    )
    pygame.draw.rect(screen, (200, 100, 100), exit_button_rect, border_radius=10)
    exit_text = FONT.render("Sair", True, (255, 255, 255))
    screen.blit(
        exit_text,
        (
            exit_button_rect.centerx - exit_text.get_width() // 2,
            exit_button_rect.centery - exit_text.get_height() // 2,
        ),
    )

    pygame.display.flip()

    return restart_button_rect, exit_button_rect


def handle_game_over(screen):
    while True:
        restart_button_rect, exit_button_rect = draw_game_over_screen(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_button_rect.collidepoint(pos):
                    return "restart"
                elif exit_button_rect.collidepoint(pos):
                    pygame.quit()
                    exit()


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
            action = handle_game_over(screen)
            if action == "restart":
                return "restart"
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


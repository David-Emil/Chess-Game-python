import pygame
import sys
import chess
from Constants import *

def create_button(x, y, width, height, text, font_size=25):
    font = pygame.font.SysFont("Segoe UI", font_size)
    return {
        'rect': pygame.Rect(x, y, width, height),
        'text': text,
        'font': font
    }

def draw_button(screen, button, is_hovered):
    color = HOVER_COLOR if is_hovered else TEXT_WHITE
    pygame.draw.rect(screen, color, button['rect'], border_radius=12)
    label = button['font'].render(button['text'], True, TEXT_BLACK)
    screen.blit(label, (
        button['rect'].x + button['rect'].width // 2 - label.get_width() // 2,
        button['rect'].y + button['rect'].height // 2 - label.get_height() // 2
    ))

def choose_mode(screen):
    title_font = pygame.font.SysFont(*FONT_BIG)
    buttons = [
        create_button(250, 250, 350, 60, "Player vs AI"),
        create_button(250, 340, 350, 60, "Player vs Player")
    ]
    
    bg_image = pygame.image.load(BG_PATH + "game-mode-bg.JPEG")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

    while True:
        screen.blit(bg_image, (0, 0))
        title = title_font.render("Game Mode", True, TEXT_BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))

        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(buttons):
            draw_button(screen, button, button['rect'].collidepoint(mouse_pos))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button['rect'].collidepoint(event.pos):
                        return "ai" if i == 0 else "pvp"

def choose_time_control(screen):
    title_font = pygame.font.SysFont(*FONT_BIG)
    buttons = []
    for i, (text, mins, inc) in enumerate(TIME_CONTROLS):
        buttons.append(create_button(250, 150 + i*70, 350, 60, text))
    
    bg_image = pygame.image.load(BG_PATH + "game-mode-bg.JPEG")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

    while True:
        screen.blit(bg_image, (0, 0))
        title = title_font.render("Time Control", True, TEXT_BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))

        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(buttons):
            draw_button(screen, button, button['rect'].collidepoint(mouse_pos))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button['rect'].collidepoint(event.pos):
                        return TIME_CONTROLS[i][1], TIME_CONTROLS[i][2]

def display_winner(screen, board, timeout=False):
    font_big = pygame.font.SysFont(*FONT_BIG)
    font_small = pygame.font.SysFont(*FONT_SMALL)
    
    screen.fill(TEXT_BLACK)
    
    if timeout:
        winner = "White Wins!" if board.turn == chess.BLACK else "Black Wins!"
        reason = "Timeout!"
    elif board.is_checkmate():
        winner = "White Wins!" if board.turn == chess.BLACK else "Black Wins!"
        reason = "Checkmate!"
    elif board.is_stalemate():
        winner = "Stalemate!"
        reason = ""
    elif board.is_insufficient_material():
        winner = "Draw by Material"
        reason = ""
    else:
        winner = "Draw!"
        reason = ""
        
    label = font_big.render(winner, True, TEXT_WHITE)
    reason_label = font_small.render(reason, True, TEXT_WHITE)
    restart = font_big.render("Press R to Restart", True, PANEL_BG)

    screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT // 2 - 50))
    if reason:
        screen.blit(reason_label, (WIDTH // 2 - reason_label.get_width() // 2, HEIGHT // 2))
    screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False
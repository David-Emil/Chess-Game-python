import pygame
import sys
import chess
import math
from Board import load_piece_images, draw_board
from Clock import ChessClock
from MinMax import minimax
from Ui import choose_mode, choose_time_control, display_winner
from Logic import GameState
from Sound import SoundManager
from Constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    # Initialize game components
    pieces_img = load_piece_images()
    sound_manager = SoundManager()
    game_state = GameState()

    # Game setup
    mode = choose_mode(screen)
    time_control_mins, increment = choose_time_control(screen)
    chess_clock = ChessClock(time_control_mins, increment) if time_control_mins > 0 else None

    if chess_clock:
        chess_clock.start()

    # Main game loop
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        hover_square = None
        if mouse_pos[0] < BOARD_WIDTH:
            col = mouse_pos[0] // SQUARE_SIZE
            row = 7 - (mouse_pos[1] // SQUARE_SIZE)
            hover_square = chess.square(col, row)

        # Draw everything
        draw_board(screen, game_state.board, pieces_img, game_state.move_history, hover_square, chess_clock, game_state.scroll_offset)
        if chess_clock:
            chess_clock.draw_timers(screen)
        pygame.display.flip()

        # Handle timeout
        if chess_clock and chess_clock.game_over:
            display_winner(screen, game_state.board, timeout=True)
            running = False
            continue

        # Check game over conditions
        if game_state.is_game_over():
            display_winner(screen, game_state.board)
            running = False
            continue

        # AI move
        if mode == "ai" and not game_state.human_turn():
            _, move = minimax(game_state.board, 3, -math.inf, math.inf, game_state.board.turn == chess.WHITE)
            if move:
                if chess_clock:
                    chess_clock.on_move()
                game_state.make_move(move)
                sound_manager.play_move_sound()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            # Handle mouse wheel for move history scrolling
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and game_state.scroll_offset > 0:  # Scroll up
                    game_state.scroll_offset -= 1
                elif event.button == 5:  # Scroll down
                    max_offset = max(0, (len(game_state.move_history) // 2) - 10)
                    if game_state.scroll_offset < max_offset:
                        game_state.scroll_offset += 1

            # Handle keyboard for move history scrolling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game_state.scroll_offset > 0:
                    game_state.scroll_offset -= 1
                elif event.key == pygame.K_DOWN:
                    max_offset = max(0, (len(game_state.move_history) // 2) - 10)
                    if game_state.scroll_offset < max_offset:
                        game_state.scroll_offset += 1

            # Human move
            if event.type == pygame.MOUSEBUTTONDOWN and (mode == "pvp" or game_state.human_turn()):
                move = game_state.handle_click(event.pos)
                if move and chess_clock:
                    chess_clock.on_move()
                    sound_manager.play_move_sound()

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

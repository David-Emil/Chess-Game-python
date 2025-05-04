import pygame
import chess
from Constants import *

def load_piece_images():
    pieces_img = {}
    for color in COLORS:
        for piece in PIECE_TYPES:
            img = pygame.image.load(f"{PIECE_IMG_PATH}{color}{piece}.png")
            pieces_img[color + piece] = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
    return pieces_img

def draw_board(screen, board, pieces_img, move_history, hover_square=None, chess_clock=None, scroll_offset=0):
    # Draw chess board
    for row in range(8):
        for col in range(8):
            color = BOARD_LIGHT if (row + col) % 2 == 0 else BOARD_DARK
            square = chess.square(col, 7 - row)
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

            if hover_square == square:
                color = HOVER_COLOR

            pygame.draw.rect(screen, color, rect)

            # Draw move highlights
            if hover_square is not None:
                piece = board.piece_at(hover_square)
                if piece and piece.color == board.turn:
                    for move in board.legal_moves:
                        if move.from_square == hover_square and move.to_square == square:
                            pygame.draw.rect(screen, MOVE_HIGHLIGHT, rect)

            # Draw pieces
            piece = board.piece_at(square)
            if piece:
                piece_key = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().upper()
                screen.blit(pieces_img[piece_key], (col * SQUARE_SIZE, row * SQUARE_SIZE))

    # Draw move history panel
    pygame.draw.rect(screen, PANEL_BG, pygame.Rect(BOARD_WIDTH, 0, HISTORY_PANEL_WIDTH, HEIGHT))
    
    font = pygame.font.SysFont(*FONT_SMALL)
    y_offset = 20
    move_pairs = [(i, i+1) for i in range(0, len(move_history), 2)]
    
    for i, (white_move, black_move) in enumerate(move_pairs[scroll_offset:scroll_offset+20]):
        move_text = f"{i + 1 + scroll_offset}. {move_history[white_move]}"
        if black_move < len(move_history):
            move_text += f" {move_history[black_move]}"
        label = font.render(move_text, True, TEXT_WHITE)
        screen.blit(label, (BOARD_WIDTH + 10, y_offset))
        y_offset += 30

    # Draw check indicator
    if board.is_check():
        font = pygame.font.SysFont(*FONT_SMALL)
        check_label = font.render("Check!", True, TIMER_RED)
        screen.blit(check_label, (10, HEIGHT - 30))
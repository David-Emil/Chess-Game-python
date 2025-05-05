import chess
from Constants import *

class GameState:
    def __init__(self):
        self.board = chess.Board()
        self.move_history = []
        self.selected_square = None
        self.scroll_offset = 0
        self.player_is_white = True
    
    def human_turn(self):
        return (self.board.turn == chess.WHITE and self.player_is_white) or \
               (self.board.turn == chess.BLACK and not self.player_is_white)
    
    def make_move(self, move):
        san = self.board.san(move)
        self.board.push(move)
        self.move_history.append(san)
        return True
    
    def is_game_over(self):
        return self.board.is_game_over()
    
    def handle_click(self, pos):
        x, y = pos
        if x < BOARD_WIDTH:
            col = x // SQUARE_SIZE
            row = 7 - (y // SQUARE_SIZE)
            clicked_square = chess.square(col, row)

            if self.selected_square is None:
                piece = self.board.piece_at(clicked_square)
                if piece and piece.color == self.board.turn:
                    self.selected_square = clicked_square
                    return None
            else:
                move = chess.Move(self.selected_square, clicked_square)
                if move in self.board.legal_moves:
                    self.make_move(move)
                    self.selected_square = None
                    return move
                self.selected_square = None
        return None
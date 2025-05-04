import time
import pygame
from Constants import *

class ChessClock:
    def __init__(self, initial_time, increment=None):
        self.initial_time = initial_time * 60  
        self.increment = increment
        self.white_time = self.initial_time
        self.black_time = self.initial_time
        self.white_turn = True
        self.last_update = None
        self.game_over = False

    def start(self):
        self.last_update = time.time()

    def on_move(self):
        if self.game_over:
            return

        current_time = time.time()
        elapsed = current_time - self.last_update

        if self.white_turn:
            self.white_time -= elapsed
            if self.increment is not None:
                self.white_time += self.increment
        else:
            self.black_time -= elapsed
            if self.increment is not None:
                self.black_time += self.increment


        if self.white_time <= 0:
            self.white_time = 0
            self.game_over = True
        elif self.black_time <= 0:
            self.black_time = 0
            self.game_over = True


        self.white_turn = not self.white_turn
        self.last_update = current_time

    def get_time(self, white=True):
        return max(0, self.white_time if white else self.black_time)

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def draw_timers(self, screen):
        font = pygame.font.SysFont(*FONT_TIMER)
        

        white_time = self.get_time(white=True)
        white_color = TIMER_RED if white_time <= 10 else TEXT_WHITE
        white_text = f"White: {self.format_time(white_time)}"
        white_label = font.render(white_text, True, white_color)
        
    
        black_time = self.get_time(white=False)
        black_color = TIMER_RED if black_time <= 10 else TEXT_WHITE
        black_text = f"Black: {self.format_time(black_time)}"
        black_label = font.render(black_text, True, black_color)
   
        timer_height = 30
        pygame.draw.rect(screen, TEXT_BLACK, (BOARD_WIDTH, 0, HISTORY_PANEL_WIDTH, timer_height))
        pygame.draw.rect(screen, TEXT_BLACK, (BOARD_WIDTH, HEIGHT - timer_height, HISTORY_PANEL_WIDTH, timer_height))
        
    
        if self.white_turn:
            pygame.draw.rect(screen, TIMER_ACTIVE_BG, (BOARD_WIDTH, 0, HISTORY_PANEL_WIDTH, timer_height))
        else:
            pygame.draw.rect(screen, TIMER_ACTIVE_BG, (BOARD_WIDTH, HEIGHT - timer_height, HISTORY_PANEL_WIDTH, timer_height))
        
    
        screen.blit(white_label, (BOARD_WIDTH + 10, (timer_height - white_label.get_height()) // 2))
        screen.blit(black_label, (BOARD_WIDTH + 10, HEIGHT - timer_height + (timer_height - black_label.get_height()) // 2))
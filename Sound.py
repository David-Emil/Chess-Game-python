import pygame
from Constants import *

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.move_sound = pygame.mixer.Sound(SOUND_PATH + "chess-move.mp3")
    
    def play_move_sound(self):
        self.move_sound.play()
# Screen dimensions
WIDTH, HEIGHT = 850, 640

# Colors
BOARD_LIGHT = "#EEEED2"
BOARD_DARK = "#769656"
HOVER_COLOR = "#6494db"
MOVE_HIGHLIGHT = "#5e96e5"
PANEL_BG = "#333333"
TEXT_WHITE = "white"
TEXT_BLACK = "black"
TIMER_RED = "red"
TIMER_ACTIVE_BG = "#444444"

# Font settings
FONT_SMALL = ("monospace", 24)
FONT_BIG = ("monospace", 50)
FONT_TIMER = ("monospace", 20, True)

# Piece types
PIECE_TYPES = ['P', 'N', 'B', 'R', 'Q', 'K']
COLORS = ['w', 'b']

# Piece values for AI
PIECE_VALUES = {
    'P': 1, 'N': 3, 'B': 3,
    'R': 5, 'Q': 9, 'K': 0
}

# Time controls (minutes, increment)
TIME_CONTROLS = [
    ("No Limit", 0, None),
    ("Bullet: 1 | 1", 1, 1),
    ("Bullet: 2 | 1", 2, 1),
    ("Blitz: 3 | 1", 3, 1),
    ("Blitz: 5 min", 5, None),
    ("Rapid: 10 min", 10, None),
    ("Rapid: 15 | 10", 15, 10)
]

# Asset paths
ASSET_DIR = "Chess project/Git-Hup/assets/"
PIECE_IMG_PATH = ASSET_DIR + "pieces/"
SOUND_PATH = ASSET_DIR + "sounds/"
BG_PATH = ASSET_DIR + "backgrounds/"

# Board settings
SQUARE_SIZE = 80
BOARD_WIDTH = 8 * SQUARE_SIZE
BOARD_HEIGHT = 8 * SQUARE_SIZE
HISTORY_PANEL_WIDTH = WIDTH - BOARD_WIDTH
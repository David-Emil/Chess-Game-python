# ♟️ Python Chess Game

A feature-rich chess implementation with dual game modes and intelligent AI, built with Pygame and python-chess.

![image](https://github.com/user-attachments/assets/a2ba65f7-3b4d-41e8-b58a-7f4edc948b94)


## 🛠️ Tech Stack
- **Frontend**: Pygame (Rendering/Input)
- **Game Logic**: python-chess (Move Validation)
- **AI**: Minimax with Alpha-Beta Pruning (Depth 3)
- **Audio**: Pygame Mixer

## 🌟 Features
- **Two Game Modes**:
  - Player vs Player (Local)
  - Player vs AI (Minimax Algorithm)
  
- **Time Controls**:
  - Bullet (1|1, 2|1)
  - Blitz (3|1, 5|0)
  - Rapid (10|0, 15|10)
  - Unlimited

- **Gameplay Enhancements**:
  - Legal move highlighting
  - Move history with scroll
  - Check/checkmate detection
  - Timeout handling
  - Move sound effects

## 📦 Project Structure
chess_project/
├── assets/
│ ├── pieces/ (wP.png, wN.png...)
│ ├── sounds/ (chess-move.mp3)
│ └── backgrounds/ (menu-bg.jpg)
├── main.py
├── constants.py
└── modules/
├── board.py # Board rendering
├── clock.py # Time management
├── ai.py # Minimax AI
├── ui.py # Menus & dialogs
├── game_logic.py # State management
└── sound.py # Audio controller


## 🚀 Installation
1. Clone repository:
bash
git clone https://github.com/your-repo/python-chess.git
cd python-chess
Install dependencies:

bash
pip install -r requirements.txt
Run the game:

bash
python main.py
Sample requirements.txt:

pygame>=2.0.0
python-chess>=1.0.0

🎮 Controls
Action	Command
Move Piece	Left Click
Scroll History	Mouse Wheel / ↑↓ Keys
Restart Game	R Key
Quit	ESC or Window Close

👥 Team Contributions
Module	Developer
Board Rendering	[Name]
Game Clock	[Name]
AI Engine	[Name]
UI System	[Name]
Sound Design	[Name]
Core Logic	[Name]

📜 Documentation
[5 David Emil Sobhi.pdf](https://github.com/user-attachments/files/20027744/5.David.Emil.Sobhi.pdf)


📸 Screenshots
![image](https://github.com/user-attachments/assets/34e07687-0016-4c73-8700-9e1c91d18b34)
![image](https://github.com/user-attachments/assets/323e1b3b-3405-45ad-ad31-3479cdcad0c8)
![image](https://github.com/user-attachments/assets/68b3536f-9c9d-4180-89eb-e6e2cc0d8bb6)
![image](https://github.com/user-attachments/assets/aa26f467-dd2e-40cc-9f74-1cda145dc7bf)
![image](https://github.com/user-attachments/assets/195a1fa6-a11b-42be-a37f-097f71ba9239)
![image](https://github.com/user-attachments/assets/56acf18e-8330-4496-ae0a-222a3410c9c3)


🌱 Future Roadmap
Online multiplayer

Enhanced AI difficulty levels

Game replay system

Customizable themes

Developed as a collaborative project to master Python game development, algorithms, and software engineering principles. Feedback and contributions welcome!

Happy Gaming! ♟️

#  Chess Game

## Overview
A classic Chess game where you play as *White* against an intelligent *AI (Black)* powered by the *Minimax algorithm with Alpha-Beta pruning*.  
- Player: White  
- AI: Black  
- Built with Python, Tkinter, and python-chess  
- Interactive GUI with clickable pieces, highlighted legal moves, and pawn promotion  

##  How to Run
1. Ensure Python 3.x is installed
    Install *Python 3.x* from [python.org](https://www.python.org/).
   
3. Install python-chess via terminal/command prompt: `pip install python-chess`  
4. Save the code as `chess_ai.py`  
5. Run the game: `python chess_ai.py`  
6. The game window will open, ready to play  

## How to Play
1. Click on a White piece to see its legal moves (highlighted in blue)  
2. Click on a highlighted square to move the piece  
3. For pawn promotion, enter a piece (`q/r/b/n`) when prompted  
4. After your move, the AI (Black) will automatically play  
5. The game ends when:  
   - A player is checkmated  
   - The game is drawn (stalemate, insufficient material, or claimable draw)  

##  Algorithm Used
*Minimax Algorithm with Alpha-Beta Pruning* ensures the AI makes strategic moves efficiently:  
- MAX player: AI maximizes its evaluation score  
- MIN player: Human minimizes AI score  
- Alpha-Beta pruning: Skips evaluating moves that cannot improve the outcome  
- Board evaluation based on *material balance* (piece values)  
- Default search depth: 2 moves ahead for quick gameplay  

##  Software & Libraries
- Python 3.x  
- Tkinter (built-in with Python)  
- python-chess  


Human vs AI Chess combines classic gameplay with intelligent AI, providing a challenging experience for players of all levels.  
The AI uses strategic evaluation to make optimal moves while keeping the game engaging and interactive.

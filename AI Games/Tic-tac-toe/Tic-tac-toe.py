# Import necessary modules
import pygame, sys, math
pygame.init()

# Constants for game layout
CELL = 130  # Each grid cell size
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🤖 Tic Tac Toe AI")

# Fonts for drawing text
font = pygame.font.Font(None, 80)
msg_font = pygame.font.Font(None, 40)
btn_font = pygame.font.Font(None, 35)

# Colors (RGB format)
BG = (250, 240, 220)       # Background color
LINE = (60, 60, 150)       # Grid line color
X_COLOR = (255, 80, 80)    # Player 'X' color
O_COLOR = (80, 120, 255)   # AI 'O' color
MSG = (0, 150, 0)          # Message text color
BTN_COLOR = (0, 120, 200)  # Button normal color
BTN_HOVER = (0, 150, 255)  # Button hover color

# Game state variables
board = [" "] * 9  # Represents 3x3 board as a list
game_over = False
message = ""


# -------------------- Drawing Section --------------------

def draw():
    """Draws the entire game screen including grid, marks, messages, and button."""
    screen.fill(BG)

    # Draw 9 cells (3x3 grid)
    for i in range(9):
        x, y = (i % 3) * CELL, (i // 3) * CELL
        rect = pygame.Rect(x, y, CELL, CELL)
        pygame.draw.rect(screen, LINE, rect, 5)

        # Draw X or O symbol if the cell is not empty
        if board[i] != " ":
            text = font.render(board[i], True, X_COLOR if board[i]=="X" else O_COLOR)
            screen.blit(text, text.get_rect(center=(x + CELL // 2, y + CELL // 2)))

    # Show result message if game is over
    if game_over:
        msg = msg_font.render(message, True, MSG)
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, 420)))

    # Draw reset button
    draw_button()
    pygame.display.flip()


def draw_button():
    """Draws the Reset button and changes color on hover."""
    global BTN_RECT
    BTN_RECT = pygame.Rect(125, 460, 150, 35)
    color = BTN_HOVER if BTN_RECT.collidepoint(pygame.mouse.get_pos()) else BTN_COLOR
    pygame.draw.rect(screen, color, BTN_RECT)
    text = btn_font.render("Reset", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=BTN_RECT.center))


# -------------------- Game Logic Section --------------------

def check_winner():
    """Checks all winning combinations and returns the winner ('X' or 'O') if any."""
    for a, b, c in [
        (0,1,2), (3,4,5), (6,7,8),   # Rows
        (0,3,6), (1,4,7), (2,5,8),   # Columns
        (0,4,8), (2,4,6)             # Diagonals
    ]:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


# -------------------- AI Section (Minimax) --------------------

def minimax(is_max):
    """
    Recursive Minimax algorithm:
    - Returns best score from the perspective of the AI ('O').
    - is_max: True for AI's turn, False for player's turn.
    """
    w = check_winner()
    if w == "O": return 1   # AI wins
    if w == "X": return -1  # Player wins
    if " " not in board: return 0  # Draw

    best = -math.inf if is_max else math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            score = minimax(not is_max)
            board[i] = " "
            best = max(best, score) if is_max else min(best, score)
    return best


def ai_turn():
    """Finds the best possible move for the AI using minimax."""
    best, move = -math.inf, None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best:
                best, move = score, i
    if move is not None:
        board[move] = "O"


# -------------------- Gameplay Control Section --------------------

def check_game_over():
    """Checks if the game has ended (win or draw) and updates message."""
    global game_over, message
    w = check_winner()
    if w:
        message = "🎉 You Win!" if w == "X" else "🤖 AI Wins!"
        game_over = True
    elif " " not in board:
        message = "😐 Draw!"
        game_over = True


def player_move(pos):
    """Handles player's move and triggers AI response."""
    if board[pos] == " " and not game_over:
        board[pos] = "X"
        check_game_over()
        if not game_over:
            ai_turn()
            check_game_over()


def reset_game():
    """Resets the game to initial state."""
    global board, game_over, message
    board, game_over, message = [" "] * 9, False, ""


# -------------------- Main Game Loop --------------------

while True:
    draw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            if BTN_RECT.collidepoint((x, y)):
                # Click on Reset button → restart game
                reset_game()
            elif y < 390:
                # Click on a cell → make a player move
                player_move((y // CELL) * 3 + (x // CELL))

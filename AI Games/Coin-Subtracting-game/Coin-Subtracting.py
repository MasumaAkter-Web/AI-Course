import pygame, sys, math

pygame.init()

# --- Window Setup ---
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Coin Subtracting Game: User vs AI")

# --- Fonts & Colors ---
font = pygame.font.Font(None, 40)       # Font for main text/buttons
msg_font = pygame.font.Font(None, 30)   # Font for messages
WHITE = (255, 255, 255)
BLUE = (50, 90, 200)   # Button color when active
RED = (220, 50, 50)    # AI turn color
GREEN = (40, 180, 60)  # Player turn color
YELLOW = (240, 200, 50)  # Coin color
DARK = (50, 50, 50)      # Background color

# --- Game State Variables ---
coins = 15                     # Total coins in the pile
message = "Your turn: Take 1, 2, or 3 coins"
game_over = False              # Flag to track game over
player_turn = True             # True if it's player's turn

# --- Minimax AI Function ---
def minimax(remaining, is_ai):
    """
    Recursive Minimax algorithm for the coin game.
    - remaining: coins left in the pile
    - is_ai: True if AI's turn, False if Player's turn
    Returns: score of the position (+1 = AI win, -1 = Player win)
    """
    if remaining == 0:
        return -1 if is_ai else 1  # If no coins left, current player loses

    moves = [1, 2, 3]  # Possible moves
    if is_ai:
        best = -math.inf
        for m in moves:
            if remaining - m >= 0:
                best = max(best, minimax(remaining - m, False))
        return best
    else:
        best = math.inf
        for m in moves:
            if remaining - m >= 0:
                best = min(best, minimax(remaining - m, True))
        return best

# --- AI Move Selection ---
def ai_move(remaining):
    """
    Determines the AI's optimal move using Minimax.
    Returns: number of coins to remove (1,2,3)
    """
    best_score = -math.inf
    move = 1
    for m in [1, 2, 3]:
        if remaining - m >= 0:
            score = minimax(remaining - m, False)
            if score > best_score:
                best_score = score
                move = m
    return move

# --- Draw Function ---
def draw():
    """
    Renders the game interface: background, coins, buttons, turn indicator, and messages.
    """
    screen.fill(DARK)
    
    # Draw turn indicator
    turn_color = GREEN if player_turn else RED
    turn_text = font.render("Your Turn" if player_turn else "AI Turn", True, turn_color)
    screen.blit(turn_text, turn_text.get_rect(center=(WIDTH//2, 40)))
    
    # Draw coins as circles in a row
    start_x = 50
    for i in range(coins):
        x = start_x + i * 35
        y = 150
        pygame.draw.circle(screen, YELLOW, (x, y), 15)
        pygame.draw.circle(screen, WHITE, (x, y), 15, 2)  # Coin outline
    
    # Draw move buttons (1,2,3 coins)
    for i, val in enumerate([1,2,3]):
        btn = pygame.Rect(100 + i*150, 300, 100, 50)
        color = BLUE if player_turn else DARK
        pygame.draw.rect(screen, color, btn)
        txt = font.render(str(val), True, WHITE)
        screen.blit(txt, txt.get_rect(center=btn.center))
    
    # Draw message below coins
    msg_text = msg_font.render(message, True, WHITE)
    screen.blit(msg_text, msg_text.get_rect(center=(WIDTH//2, 250)))
    
    pygame.display.flip()

# --- Main Game Loop ---
while True:
    draw()  # Refresh screen each frame
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Handle player clicking on move buttons
        if e.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            x, y = e.pos
            for i, val in enumerate([1,2,3]):
                btn = pygame.Rect(100 + i*150, 300, 100, 50)
                if btn.collidepoint(x,y) and coins - val >= 0:
                    coins -= val
                    if coins == 0:
                        message = "You took the last coin. You lose!"
                        game_over = True
                    else:
                        player_turn = False
                        message = f"You took {val}. AI's turn."
        
        # AI's turn
        if not player_turn and not game_over:
            pygame.time.delay(500)  # Delay for better visual effect
            ai = ai_move(coins)
            coins -= ai
            if coins == 0:
                message = f"AI took {ai} and last coin. AI loses! You win!"
                game_over = True
            else:
                player_turn = True
                message = f"AI took {ai}. Your turn."
        
        # Reset game if 'R' is pressed after game over
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r and game_over:
                coins = 15
                message = "Your turn: Take 1, 2, or 3 coins"
                game_over = False
                player_turn = True

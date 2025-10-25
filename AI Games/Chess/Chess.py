import tkinter as tk
from tkinter import simpledialog, messagebox
import chess, math

# ==== CONFIG ====
AI_DEPTH, SQUARE_SIZE = 2, 72
COLORS = {
    "select": "#FFD54F", "legal": "#90CAF9",
    "light": "#F0D9B5", "dark": "#B58863"
}
FONT = ("Segoe UI Symbol", 40)

PIECE_VALUES = {
    chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330,
    chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 20000
}
PIECE_SYMBOLS = {
    chess.PAWN: ('♙', '♟'), chess.KNIGHT: ('♘', '♞'),
    chess.BISHOP: ('♗', '♝'), chess.ROOK: ('♖', '♜'),
    chess.QUEEN: ('♕', '♛'), chess.KING: ('♔', '♚')
}

# ==== CHESS AI ====
def evaluate_board(board):
    return sum(val * (len(board.pieces(pt, chess.BLACK)) -
                      len(board.pieces(pt, chess.WHITE)))
               for pt, val in PIECE_VALUES.items())

def evaluate_terminal(board, depth):
    if board.is_checkmate():
        return 100000 - depth if board.turn == chess.WHITE else -100000 + depth
    return 0 if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_draw() else None

def minimax(board, depth, alpha, beta, maximize):
    term = evaluate_terminal(board, depth)
    if term is not None: return term
    if depth == 0: return evaluate_board(board)

    best = -math.inf if maximize else math.inf
    for mv in board.legal_moves:
        board.push(mv)
        val = minimax(board, depth - 1, alpha, beta, not maximize)
        board.pop()
        if maximize:
            best = max(best, val); alpha = max(alpha, val)
        else:
            best = min(best, val); beta = min(beta, val)
        if beta <= alpha: break
    return best

def best_move(board, depth=AI_DEPTH):
    best, move = -math.inf, None
    for mv in board.legal_moves:
        board.push(mv)
        score = minimax(board, depth - 1, -math.inf, math.inf, False)
        board.pop()
        if score > best:
            best, move = score, mv
    return move

# ==== UI SETUP ====
board = chess.Board()
selected, legal_moves = None, []

root = tk.Tk()
root.title("♟ Human vs AI Chess")
canvas = tk.Canvas(root, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE, highlightthickness=0)
canvas.pack()
tk.Label(root, text="You: White  —  AI: Black", font=("Arial", 12)).pack(fill="x")

def coord_to_square(x, y):
    c, r = x // SQUARE_SIZE, 7 - (y // SQUARE_SIZE)
    return chess.square(c, r) if 0 <= c < 8 and 0 <= r < 8 else None

def draw_board():
    canvas.delete("all")
    for r in range(8):
        for c in range(8):
            sq = chess.square(c, 7 - r)
            x1, y1 = c*SQUARE_SIZE, r*SQUARE_SIZE
            color = COLORS["select"] if sq == selected else \
                    COLORS["legal"] if sq in legal_moves else \
                    COLORS["light"] if (r + c) % 2 == 0 else COLORS["dark"]
            canvas.create_rectangle(x1, y1, x1+SQUARE_SIZE, y1+SQUARE_SIZE, fill=color, outline="")
            p = board.piece_at(sq)
            if p:
                sym = PIECE_SYMBOLS[p.piece_type][0 if p.color else 1]
                canvas.create_text(x1 + SQUARE_SIZE//2, y1 + SQUARE_SIZE//2,
                                   text=sym, font=FONT, fill="black" if (r + c) % 2 == 0 else "white")
    for i, ch in enumerate("abcdefgh"):
        canvas.create_text(i*SQUARE_SIZE + 4, 8*SQUARE_SIZE - 14, text=ch, anchor="w", font=("Arial", 9))

def show_result():
    if board.is_checkmate():
        winner = "Black (AI)" if board.turn == chess.WHITE else "White (You)"
        messagebox.showinfo("Game Over", f"Checkmate! Winner: {winner}")
    elif board.is_stalemate() or board.is_insufficient_material():
        messagebox.showinfo("Game Over", "Draw!")

def on_click(e):
    global selected, legal_moves
    sq = coord_to_square(e.x, e.y)
    if not sq: return

    if selected is None:
        p = board.piece_at(sq)
        if p and p.color == chess.WHITE:
            selected = sq
            legal_moves = [m.to_square for m in board.legal_moves if m.from_square == sq]
    else:
        mv = None
        if board.piece_at(selected).piece_type == chess.PAWN and chess.square_rank(sq) in (0, 7):
            promo = simpledialog.askstring("Promote to", "(q/r/b/n):", parent=root)
            if promo and promo.lower() in "qrbn":
                mv = chess.Move(selected, sq, promotion={'q':chess.QUEEN,'r':chess.ROOK,'b':chess.BISHOP,'n':chess.KNIGHT}[promo.lower()])
        else:
            mv = chess.Move(selected, sq)
        if mv in board.legal_moves:
            board.push(mv)
            selected, legal_moves = None, []
            draw_board()
            if board.is_game_over(): return show_result()
            root.after(150, ai_move)
        else:
            selected, legal_moves = None, []
    draw_board()

def ai_move():
    if board.is_game_over(): return show_result()
    mv = best_move(board)
    if mv: board.push(mv)
    draw_board()
    if board.is_game_over(): show_result()

canvas.bind("<Button-1>", on_click)
draw_board()
root.mainloop()

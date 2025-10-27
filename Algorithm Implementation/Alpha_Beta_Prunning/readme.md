# Alpha-Beta Pruning Algorithm

##  How the Algorithm Works
Alpha-Beta Pruning is an optimization technique for the Minimax algorithm used in decision-making and game theory.  
It reduces the number of nodes that are evaluated in the search tree by "pruning" branches that cannot possibly affect the final decision.

## Steps:
1. The algorithm recursively explores the game tree using the Minimax strategy (alternating between maximizing and minimizing players).  
2. Two variables are maintained:
   - Alpha (α): Best value that the maximizer currently can guarantee.
   - Beta (β): Best value that the minimizer currently can guarantee.  
3. If β ≤ α, further exploration along that branch is pruned (stopped), since it won’t affect the outcome.  
4. The process continues until all possible paths are explored or pruned.  
5. The algorithm returns the best achievable value and the corresponding path.

##  Applications
Alpha-Beta Pruning is used mainly in:
- Two-player games (Chess, Tic-Tac-Toe, Checkers, etc.)  
- Game AI for decision-making  
- Search problems in adversarial environments  
- Real-time strategy games to optimize move evaluation  


## ⏱️ Complexity
1.Time Complexity: O(b^(d/2)) — where *b* is the branching factor and *d* is the depth.  
  > (Much faster than the regular Minimax O(b^d))  
2.Space Complexity: O(b * d) — due to recursive calls and tree storage.

<img width="1366" height="768" alt="Screenshot (100)" src="https://github.com/user-attachments/assets/69f351df-37f4-4d01-b31a-bea531c7ea76" />Screenshot (100).png




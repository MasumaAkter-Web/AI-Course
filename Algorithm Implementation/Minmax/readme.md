#  Minimax Algorithm

##  How the Algorithm Works
The Minimax algorithm is a decision-making algorithm used in two-player games like Chess, Tic-Tac-Toe, etc.  
It aims to minimize the possible loss in a worst-case scenario — hence the name Minimax.

## Working Steps:
1. The algorithm simulates all possible game moves using a game tree.  
2. The tree has two types of players:
   - MAX player:Tries to get the maximum score.
   - MIN player: Tries to minimize the score.  
3. The algorithm alternates between maximizing and minimizing levels recursively.  
4. Leaf nodes contain the utility (score) values of terminal states.  
5. The value is then propagated upward — each MAX node takes the maximum of its children, and each MIN node takes the minimum.  
6. Finally, the best possible value and path are returned for the MAX player.

##  Applications
Minimax Algorithm is widely used in:
- Game-playing AI (Chess, Tic-Tac-Toe, Checkers, etc.)  
- Decision-making systems involving adversarial conditions  
- Pathfinding and strategy optimization in AI agents  
- Turn-based simulation games

## Complexity
1.Time Complexity: O(b^d)  
  - 'b' = branching factor (number of moves per node)  
  - 'd' = depth of the tree  
2.Space Complexity: O(b * d)  
  - Due to recursion and storage of child nodes.
  - <img width="1366" height="768" alt="Screenshot (101)" src="https://github.com/user-attachments/assets/2f031670-c7bc-4b8d-b89c-6ee3821bdfc9" />Screenshot (101).png


    

  



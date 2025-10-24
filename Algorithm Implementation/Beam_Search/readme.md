#  Beam Search Algorithm

## How the Algorithm Works
Beam Search is a heuristic-based search algorithm that explores the graph in levels while keeping only a fixed number (beam width) of the most promising nodes at each level.  
It is a memory-efficient variation of the Best-First Search algorithm.

## Steps:
1. Start from the initial node and add it to the queue.  
2. Expand all nodes at the current level and generate their neighbors.  
3. Sort all generated nodes using the heuristic function (lower value = better).  
4. Keep only the best `beam_width` nodes and discard the rest.  
5. Continue expanding until the goal is found or no nodes remain.  
6. Display the visited nodes and the final path.

##  Applications
- Natural Language Processing (e.g., machine translation, text generation)  
- Speech recognition  
- Game AI decision-making  
- Optimization and scheduling problems  

##  Complexity
1.Time Complexity: O(bᵈ) — where 'b' = beam width, 'd' = search depth  
2.Space Complexity: O(b) — only a limited number of nodes are stored  

> Beam Search trades **accuracy for speed** — smaller beam widths run faster but may miss the optimal path.



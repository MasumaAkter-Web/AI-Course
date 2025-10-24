#  Best First Search (Greedy Search) Algorithm

##  How the Algorithm Works
Best First Search is a heuristic-based search algorithm that explores a graph by always expanding the node that appears to be closest to the goal according to a given heuristic function.  
It uses a priority queue where nodes are sorted based on their heuristic values (the lower the value, the more promising the node).

## Steps:
1. Start with the initial node and add it to the queue.  
2. Select the node with the lowest heuristic value.  
3. Mark it as visited and expand its neighbors.  
4. Add all unvisited neighbors to the queue.  
5. Repeat until the goal node is found or no nodes remain.  
6. Display the visited nodes and the final path.

##  Applications
Best First Search is used in various AI and optimization problems, including:
- Pathfinding in maps and navigation systems  
- Puzzle-solving (e.g., 8-puzzle, maze traversal)  
- Network routing and data packet optimization  
- Game AI — selecting most promising moves based on heuristics  


##  Complexity
  1.Time Complexity: O(E) in the worst case (depends on the heuristic and graph size)  
  2.Space Complexity: O(V) for storing the queue and visited nodes  

> It is not guaranteed to find the optimal path, as it relies solely on heuristic estimates.



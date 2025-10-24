#  DFS (Depth-First Search) Algorithm

## How the Algorithm Works
Depth-First Search (DFS) is a graph traversal algorithm that explores nodes as deep as possible along each branch before backtracking. It uses a stack (LIFO), either explicitly or via recursion.

### Steps:
1. Start from a given node. 
2. Add the starting node to the stack and mark it as visited.  
3. While the stack is not empty:  
   - Pop the top node from the stack.  
   - Process or print the node.  
   - Push all unvisited neighbors onto the stack (reversed order if you want a specific traversal).  
4. Repeat until all reachable nodes are visited.

## Applications
DFS is used in:  
- Detecting cycles in graphs  
- Topological sorting of nodes  
- Solving mazes and puzzles  
- Pathfinding in AI and games  
- Checking graph connectivity

##  Complexity
1.Time Complexity: O(V + E) — V = vertices, E = edges  
2.Space Complexity: O(V) — for stack and visited list






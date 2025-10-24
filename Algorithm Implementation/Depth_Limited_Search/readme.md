#  DLS (Depth-Limited Search) Algorithm

## How the Algorithm Works
Depth-Limited Search (DLS) is a modified version of DFS where the search is limited to a maximum depth. It explores nodes as deeply as possible along each branch but does not go beyond the depth limit. This prevents infinite loops in graphs with cycles.

## Steps:
1. Start from a given node.  
2. Add the starting node to a stack with depth 0.  
3. While the stack is not empty:  
   - Pop a node and its depth from the stack.  
   - If the node is unvisited and within the depth limit, mark it as visited.  
   - If the node is the 'target', stop and print the path.  
   - Push all unvisited neighbors onto the stack with incremented depth.  
4. If the stack is empty and the target is not found, report that it was not found within the depth limit

## Applications
DLS is used in:  
- Avoiding infinite loops in DFS  
- Solving AI puzzles with depth constraints  
- Searching in large or infinite graphs  
- Implementing Iterative Deepening Search (IDS)

## Complexity
1.Time Complexity:** O(b^l) — b = branching factor, l = depth limit  
2.Space Complexity:** O(l) — stores nodes along a single path (stack)





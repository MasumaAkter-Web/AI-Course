
#  IDS (Iterative Deepening Search) Algorithm

##  How the Algorithm Works
Iterative Deepening Search (IDS) is a combination of BFS and DFS. It performs a series of Depth-Limited Searches (DLS) with increasing depth limits until the target node is found. IDS explores nodes like DFS (low memory usage) but guarantees finding the shortest path like BFS.

### Steps:
1. Start from the initial node.  
2. Set a depth limit, starting from 0 and increasing iteratively.  
3. Perform a Depth-Limited Search (DLS) for the current limit:  
   - Explore nodes deeply along a branch but do not exceed the limit.  
   - If the target node is found, stop and return the path.  
4. Increase the depth limit and repeat until the maximum limit is reached or the target is found.  
5. If the target is not found within the maximum limit, report failure.

##  Applications
IDS is used in:  
- AI search problemswhere memory is limited  
- Game-solving algorithms (chess, puzzles)  
- Robotics pathfinding
- When the depth of solution is unknown but a reasonable maximum exists  

## Complexity
1.Time Complexity: O(b^d) — b = branching factor, d = depth of solution  
2.Space Complexity: O(d) — stores nodes along a single path (stack)
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ddc7f6ca-6a26-4f24-9159-34d362c21529" />.png



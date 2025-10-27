#  A* Search Algorithm

## How the Algorithm Works
A* Search is a heuristic-based graph traversal algorithm used to find the shortest path from a start node to a goal node.  
It combines path cost (g) and heuristic estimate (h) to prioritize nodes using the formula:  
f(n) = g(n) + h(n)
Where:  
- g(n) = cost from start node to current node  
- h(n) = estimated cost from current node to goal node (heuristic)

### Steps:
1. Start from the initial node and calculate `f = g + h`.  
2. Maintain a priority queue sorted by `f` values.  
3. Expand the node with the lowest f value.  
4. Add neighbors to the queue with updated costs.  
5. Repeat until the goal node is reached.  
6. Print the path and total cost.

##  Applications
A* Search is widely used in:  
- Shortest path finding in maps and graphs  
- AI pathfinding in games (e.g., NPC movement)  
- Robotics navigation  
- Route optimization and GPS systems

## Complexity
1.Time Complexity: O(E) in the worst case — depends on graph size and heuristic  
2.Space Complexity: O(V) — stores all visited nodes and queue elements  

*The efficiency of A* heavily depends on the quality of the heuristic.  

  <img width="1366" height="768" alt="Screenshot (97)" src="https://github.com/user-attachments/assets/aa0edb0e-9cf7-49fa-b774-e4e127fd1ff4" />Screenshot (97).png

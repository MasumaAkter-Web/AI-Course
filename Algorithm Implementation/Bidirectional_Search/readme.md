#  BDS (Bidirectional Search) Algorithm

##  How the Algorithm Works
Bidirectional Search (BDS) is a graph search algorithm that runs two simultaneous searches:  
- One forward from the start node  
- One backward from the goal node
The searches continue until they meet in the middle, reducing the search space compared to standard BFS.

##  Steps:
1. Initialize two sets: frontier from start and frontier from goal.  
2. Expand nodes alternately from both frontiers.  
3. If the frontiers intersect, a path exists and the search stops.  
4. If either frontier is empty without intersection, there is no path.

## Applications
BDS is used in:  
- Shortest path finding in graphs  
- Network routing and communication problems  
- AI pathfinding in games and robotics  
- Social network analysis (finding connections faster)  


##  Complexity
1.Time Complexity: O(b^(d/2)) — b = branching factor, d = depth of solution  
2Space Complexity: O(b^(d/2)) — stores nodes for both frontiers  

**BDS is faster than BFS for large graphs because it searches from both ends simultaneously.
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b991157d-e82e-4509-869b-b03dcea0ba60" />.png



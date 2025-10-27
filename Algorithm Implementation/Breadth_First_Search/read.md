# BFS (Breadth-First Search) Algorithm

## Overview
Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes level by level, starting from a selected node. It uses a queue (FIFO) to manage the nodes to be visited, ensuring that all neighbors at the current level are explored before moving deeper into the graph.

## Steps:
1. Select a starting node.  
2. Add the starting node to the queue and mark it as visited.  
3. While the queue is not empty:  
   - Dequeue the front node.  
   - Process or print the node.  
   - Enqueue all unvisited neighboring nodes.  
4. Continue until all reachable nodes have been visited.

##  Applications
BFS is widely used in:  
- Finding the shortest path in unweighted graphs  
- Social network analysis (e.g., finding connections/friends)  
- Web crawlers to index pages  
- Network routing and broadcasting  
-AI problem-solving such as puzzle or game-solving

##  Complexity
1.Time Complexity: O(V + E) — V = number of vertices, E = number of edges
2.Space Complexity: O(V) — space used by the queue and visited nodes

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/23a9907c-0a46-46f6-ba9a-914d3e03752b" />.png



# Smart Network Logistics Engine (SNLE)

## Student Information
Name: [Jashanpreet Singh]  
Student ID: [300209772]  

---

## Project Description

This project implements a Smart Network Logistics Engine that models a delivery network using a directed weighted graph.

Nodes represent depots, warehouses, or delivery locations.  
Edges represent routes with associated costs (distance or time).

The system allows:
- Building a network from a file
- Finding shortest delivery routes
- Detecting cycles in the network
- Managing priority-based dispatch queues
- Searching nodes using prefix matching
- Looking up depot information

---

## Features Implemented

### 1. Graph Construction
- Directed weighted graph using adjacency list
- Built from input file (`data/network.txt`)

### 2. Shortest Path (Dijkstra)
- Computes shortest distances
- Also returns the actual path between nodes

### 3. Cycle Detection
- Uses DFS with color marking (WHITE, GRAY, BLACK)

### 4. Priority Dispatch Queue
- Implemented using a MaxHeap
- Ensures highest priority packages are processed first

### 5. Depot Lookup (Hash Map)
- Stores node information
- Provides fast lookup (O(1) average)

### 6. Route Prefix Search (Trie)
- Supports searching node names by prefix


## How to Run

- 1. Open terminal  
- 2. Navigate to project folder:
    - cd comp251-capstone

## run the program
- python3 src/main.py

## Sample Input (data/network.txt)
A B 5
A C 2
B D 1
C D 4

## Sample Output
Example (shortest path from A to D):

Shortest path: A -> C -> D
Total cost: 6


## Complexity Analysis

### Graph Construction
- Time: O(V + E)

### Dijkstra Algorithm
- Time: O(V²)
- Space: O(V)

### Cycle Detection (DFS)
- Time: O(V + E)
- Space: O(V)

### MaxHeap
- Insert: O(log n)
- Extract Max: O(log n)

### HashMap
- Insert: O(1)
- Lookup: O(1)

### Trie
- Insert: O(L)
- Prefix Search: O(L + N)

# Where:
- V = number of nodes
- E = number of edges
- L = length of word
- N = number of results

## Challenges Faced
- Understanding and implementing multiple data structures  
- Connecting all modules into one working system  
- Handling user input and file parsing correctly  


## Conclusion
This project demonstrates how multiple data structures and algorithms can be integrated into a practical system for solving real-world logistics problems.
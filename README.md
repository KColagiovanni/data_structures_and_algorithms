# Data Structures and Algorithms

### Description:
Show how to implement different data structures and algorithms, explain when to use each, and compare time complexity of each. 

### Overview of Data Structures and Algorithms implemented in this project:
#### Data Structures:
* Record
* Array
* Linked List
* Binary Tree
* Hash Table
* Min Heap
* Graph
* Weighted Graph

#### Algorithms:
* Insert/Append
* Delete/Pop
* Search
  * Linear
  * Binary
  * Depth First
  * Breadth First
  * Hash-Based
* Traverse/Print Elements
* Size/Count Elements

### Details and Use Case Explanations:
#### Record:
* **Use Case**: Store and manage structured data (e.g., employee record, configuration settings). 
* **Advantages**: Simple, fixed fields; easy attribute access. 
* **Disadvantages**: Not suitable for collections or scalable datasets.

#### Array:
* **Use Case**: Fast indexed access (e.g., list of sensor readings, matrix data). 
* **Advantages**: Contiguous memory; great for indexed operations and sorting. 
* **Disadvantages**: Costly insertion/deletion in middle; resizing overhead. 
* ✅ Preferred when you need random access and data is mostly static.

#### Linked List:
* **Use Case**: Dynamic, sequential data (e.g., task queue, undo stack). 
* **Advantages**: Efficient insert/delete anywhere if reference known.
* **Disadvantages**: No random access; linear traversal for search.
* ✅ Preferred for dynamic structures where size changes frequently.

#### Binary Tree:
* **Use Case**: Hierarchical data (e.g., family tree, file system, expression tree). 
* **Advantages**: Sorted data storage (in BST), balanced trees give log-time ops. 
* **Disadvantages**: Needs balancing to maintain efficiency. 
* ✅ Used in searching, sorting (e.g., BSTs, AVL, Red-Black Trees).

#### Hash Table:
* **Use Case**: Fast key-value storage (e.g., symbol tables, caches, lookup tables).
* **Advantages**: Constant-time insert/search/delete average. 
* **Disadvantages**: Collisions and resizing can affect performance. 
* ✅ Preferred for fast lookups and when order doesn’t matter.

#### Min Heap:
* **Use Case**: Prioritization (e.g., task scheduling, shortest-path algorithms). 
* **Advantages**: Quick access to smallest/largest element. 
* **Disadvantages**: Not efficient for random element lookup. 
* ✅ Used in priority queues, Dijkstra’s algorithm, median tracking.

#### Graph:
* **Use Case**: Model relationships, connections, or networks (e.g., social networks, transport).
* **Advantages**: Can represent complex relationships. 
* **Disadvantages**: Higher memory usage; algorithms are more complex. 
* ✅ Used for BFS, DFS, connectivity checks.

#### Weighted Graph:
* **Use Case**: Network optimization (e.g., GPS routing, communication networks). 
* **Advantages**: Captures cost/distance/priority in relationships. 
* **Disadvantages**: Heavier computational algorithms (e.g., Dijkstra, Bellman-Ford). 
* ✅ Used when edge costs matter, not just connectivity.


### Comparisons:

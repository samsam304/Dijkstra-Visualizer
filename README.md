Dijkstra-Visualizer

This project implements a visual and functional simulation of Dijkstra’s shortest path algorithm on randomly generated graphs using Python and NetworkX. It highlights shortest paths and provides visualization through Matplotlib.

Project Structure

Main.py

Entry point of the program. Generates a random graph based on provided characteristics, runs Dijkstra's algorithm from a start node, and displays both the graph and its shortest path tree.

GraphGenerator.py

Containing the RandomGraph class that generates a strongly connected, weighted graph, provides methods to visualize the graph and highlights the shortest path tree. It also inverts edge weights to enhance layout clarity in visualizations.

DijkstraTraversal.py

Implements Dijkstra’s algorithm using a priority queue (heapq) to compute the shortest path tree from a given start node.

Functionallity:

Generate a random connected graph with 8 nodes.
Compute shortest paths from node 0.

Display:

The graph with all edges and weights.
The shortest path tree highlighted in red.
The shortest distances from each node in dictionary format.
The shortest path tree in dictionary format. 

Customization

You can change parameters in Main.py:

num_nodes = 8          # Change the size of the graph

weight_range = (1, 5)  # Adjust edge weight bounds

start_node = 0         # Select a different starting node

License

This project is provided for educational and visualization purposes. Feel free to modify and extend it for personal or academic use.

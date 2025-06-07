"""
Dijkstra's algorithm for shortest paths.
:param graph: The NetworkX graph.
:param start_node: The starting node for the algorithm.
:return: A tuple containing:
    - distances: A dictionary of the shortest distances to each node.
    - shortest_path: A dictionary showing the path tree.
"""

import heapq

# Implementing Dijkstra's Algorithm
def dijkstra(graph, start_node):
    # Initialize distances with infinity and the priority queue
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]  # (distance, node)

    # Initialize a dictionary to keep track of the shortest path
    shortest_path = {node: None for node in graph.nodes()}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip nodes that have already been visited with shorter distances
        if current_distance > distances[current_node]:
            continue

        # Explore the neighbors
        for neighbor, edge_attributes in graph[current_node].items():
            weight = edge_attributes['weight']
            distance = current_distance + weight

            # Only consider this new path if it's shorter than the known distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_path
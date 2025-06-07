from GraphGenerator import RandomGraph
from DijkstraTraversal import dijkstra

def main():
    num_nodes = 8
    weight_range = (1, 5)
    start_node = 0

    # Create a random graph instance
    random_graph = RandomGraph(num_nodes, weight_range)
    graph = random_graph.get_graph()

    # Run Dijkstra's algorithm on the generated graph
    distances, shortest_path = dijkstra(graph, start_node)

    print(f"Shortest distances from node {start_node}: {distances}")
    print(f"Shortest path tree: {shortest_path}")

    # Visualize the graph
    random_graph.draw()

    # Draw the graph with highlighted shortest path
    random_graph.draw_shortest_path(start_node, distances, shortest_path)

if __name__ == "__main__":
    main()
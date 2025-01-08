def dijkstra(graph, start):
    """
    Implements Dijkstra's shortest path algorithm.
    
    Parameters:
    graph: dict of dict
        A dictionary where keys are nodes and values are dictionaries of neighboring nodes and their distances
        Example: {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'D': 3},
            'C': {'A': 2, 'D': 1},
            'D': {'B': 3, 'C': 1}
        }
    start: str
        The starting node
    
    Returns:
    tuple (distances, previous)
        distances: Dictionary of shortest distances from start to each node
        previous: Dictionary of previous nodes in the optimal path
    """
    # Initialize distances with infinity for all nodes except start
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Dictionary to store the previous node in optimal path
    previous = {node: None for node in graph}
    
    # Set of unvisited nodes
    unvisited = set(graph.keys())
    
    while unvisited:
        # Find the unvisited node with minimum distance
        current = min(unvisited, key=lambda node: distances[node])
        
        # If we're finding infinity, then remaining nodes are unreachable
        if distances[current] == float('infinity'):
            break
            
        # Remove the current node from unvisited set
        unvisited.remove(current)
        
        # Check each neighbor of current node
        for neighbor, weight in graph[current].items():
            if neighbor in unvisited:
                # Calculate new distance to neighbor
                distance = distances[current] + weight
                
                # If we found a shorter path, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
    
    return distances, previous

def get_shortest_path(previous, start, end):
    """
    Reconstructs the shortest path from start to end nodes.
    
    Parameters:
    previous: dict
        Dictionary of previous nodes from dijkstra()
    start: str
        Starting node
    end: str
        End node
    
    Returns:
    list
        The shortest path from start to end
    """
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
        
    # Return reversed path (from start to end)
    return path[::-1]

# Example usage
if __name__ == "__main__":
    # Example graph
    example_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 3},
        'C': {'A': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }
    
    # Find shortest paths from node 'A'
    start_node = 'A'
    distances, previous = dijkstra(example_graph, start_node)
    
    # Print shortest distances from A to all nodes
    print(f"Shortest distances from {start_node}:")
    for node, distance in distances.items():
        print(f"{start_node} -> {node}: {distance}")
    
    # Example: find path from A to D
    path = get_shortest_path(previous, 'A', 'D')
    print(f"\nShortest path from A to D: {' -> '.join(path)}")
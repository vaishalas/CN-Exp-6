import heapq

# Distance Vector Routing
class DistanceVectorRouter:
    def __init__(self, nodes):
        self.nodes = nodes
        self.distance_vectors = {node: {neighbor: float('inf') for neighbor in nodes} for node in nodes}
        for node in nodes:
            self.distance_vectors[node][node] = 0

    def add_link(self, src, dest, cost):
        self.distance_vectors[src][dest] = cost
        self.distance_vectors[dest][src] = cost

    def update_routing_table(self):
        for _ in range(len(self.nodes)):
            for src in self.nodes:
                for dest in self.nodes:
                    if src != dest:
                        for neighbor in self.nodes:
                            if self.distance_vectors[src][dest] > self.distance_vectors[src][neighbor] + self.distance_vectors[neighbor][dest]:
                                self.distance_vectors[src][dest] = self.distance_vectors[src][neighbor] + self.distance_vectors[neighbor][dest]

# Link State Routing (Dijkstra's Algorithm)
class LinkStateRouter:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: {} for node in nodes}

    def add_link(self, src, dest, cost):
        self.graph[src][dest] = cost
        self.graph[dest][src] = cost

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

# Example usage
def run_routing():
    nodes = ['A', 'B', 'C', 'D']

    # Distance Vector Routing
    print("Distance Vector Routing:")
    dv_router = DistanceVectorRouter(nodes)
    dv_router.add_link('A', 'B', 1)
    dv_router.add_link('A', 'C', 4)
    dv_router.add_link('B', 'C', 2)
    dv_router.add_link('B', 'D', 5)
    dv_router.add_link('C', 'D', 1)
    dv_router.update_routing_table()
    for node in nodes:
        print(f"Node {node} Distance Vector: {dv_router.distance_vectors[node]}")
    
    # Link State Routing
    print("\nLink State Routing (Dijkstra's Algorithm):")
    ls_router = LinkStateRouter(nodes)
    ls_router.add_link('A', 'B', 1)
    ls_router.add_link('A', 'C', 4)
    ls_router.add_link('B', 'C', 2)
    ls_router.add_link('B', 'D', 5)
    ls_router.add_link('C', 'D', 1)
    for node in nodes:
        shortest_paths = ls_router.dijkstra(node)
        print(f"Shortest paths from {node}: {shortest_paths}")

run_routing()

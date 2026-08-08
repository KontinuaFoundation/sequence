import kpqueue

class Node:
    def __init__(self, label):
        self.label = label
        self.edges = []

    # For prettier prints
    def __repr__(self):
        return f"(node:{self.label}, edges:{len(self.edges)})"
    
    # Nodes will be ordered by their location in memory
    def __lt__(self, other):
        return id(self) < id(other)
    

class WeightedEdge:
    def __init__(self, cost, node_a, node_b):
        self.cost = cost
        self.node_a = node_a
        node_a.edges.append(self)
        self.node_b = node_b
        node_b.edges.append(self)

    def other_end(self, node_from):
        if self.node_a == node_from:
            return self.node_b
        else:
            return self.node_a

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, new_node):
        self.nodes.append(new_node)

    def __repr__(self):
        return f"(Graph:{self.nodes})"

    def cost_from_node(self, origin_node):

        # Cost of cheapest path from origin node discovered so far
        seen_dist = {}

        # The distance from the origin node to itself is zero
        seen_dist[origin_node] = 0.0

        # When visited, we can record the final distance here
        finalized_dist = {}

        # Make a priority queue and put the origin node in
        pqueue = kpqueue.PriorityQueue()
        pqueue.add(origin_node, 0.0)

        # The previous city on that cheapest path
        prev = {}

        # While there are still nodes in the queue
        while pqueue:

            # Get unvisited node with lowest cost
            (current_node_cost, current_node) = pqueue.pop()
            finalized_dist[current_node] = current_node_cost
            del seen_dist[current_node]

            # Update all the unvisited neighbors
            for edge in current_node.edges:

                # What node is at the other end of this edge?
                v = edge.other_end(current_node)

                # Visited nodes are already minimized, skip them
                if v in finalized_dist:
                    continue

                # What is the cost to this neighbor?
                alt = current_node_cost + edge.cost

                # Is this the first time I am seeing the node?
                if v not in seen_dist:

                    # Insert into the seen_dict, prev, and priority queue
                    seen_dist[v] = alt
                    prev[v] = current_node
                    pqueue.add(v, alt)

                else: # v has been seen. Is this a cheaper route?
                    old_dist = seen_dist[v]
                    if alt < old_dist:
                        # Update the seen_dict, prev, and priority queue
                        seen_dist[v] = alt
                        prev[v] = current_node
                        pqueue.update(v, old_dist, alt)

        return (finalized_dist, prev)

def shortest_path(prev, destination):

    # Include the destination in the path
    path = [destination]
    current_node = destination

    # Keep stepping backward in the path
    while current_node in prev:

        # What node should come before the current node?
        previous_node = prev[current_node]

        # Insert it at the start of the list
        path.insert(0, previous_node)
        current_node = previous_node

    return path

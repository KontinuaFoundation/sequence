import math

# Each router lists its neighbors and the delay (in ms) of each link
links = {
    "A": {"B": 5, "C": 7},
    "B": {"A": 5, "C": 3, "D": 13},
    "C": {"A": 7, "B": 3, "E": 4},
    "D": {"B": 13, "E": 6, "F": 2},
    "E": {"C": 4, "D": 6, "F": 15},
    "F": {"D": 2, "E": 15},
}

def dijkstra(links, origin):
    dist = {router: math.inf for router in links}
    dist[origin] = 0
    prev = {}
    unvisited = set(links)
    while unvisited:
        current = min(unvisited, key=lambda r: dist[r])
        if dist[current] == math.inf:
            break
        unvisited.remove(current)
        for neighbor, delay in links[current].items():
            if dist[current] + delay < dist[neighbor]:
                dist[neighbor] = dist[current] + delay
                prev[neighbor] = current
    return dist, prev

def forwarding_table(links, router):
    dist, prev = dijkstra(links, router)
    table = {}
    for destination in sorted(links):
        if destination == router or destination not in prev:
            continue
        # Walk back from the destination until the step just after the router
        hop = destination
        while prev[hop] != router:
            hop = prev[hop]
        table[destination] = (hop, dist[destination])
    return table

def show(table):
    for destination, (hop, cost) in table.items():
        print(f"  to {destination}: send to {hop}  ({cost} ms)")

print("Router A's forwarding table:")
show(forwarding_table(links, "A"))

# The link between C and E breaks
del links["C"]["E"]
del links["E"]["C"]
print("After the C-E link fails:")
show(forwarding_table(links, "A"))

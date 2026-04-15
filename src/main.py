from graph import Graph
from dijkstra import dijkstra
from cycle_detection import has_cycle
from maxheap import MaxHeap
from hashmap import DepotMap
from trie import Trie
from dijkstra import dijkstra, get_path


def load_graph(filename):
    g = Graph()

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) == 3:
                start = parts[0]
                end = parts[1]
                weight = int(parts[2])
                g.add_edge(start, end, weight)

    return g


def build_trie_from_graph(graph):
    trie = Trie()
    for node in graph.graph:
        trie.insert(node)
    return trie


def build_depot_map(graph):
    depot_map = DepotMap()
    for node in graph.graph:
        depot_map.add_depot(node, {"name": node})
    return depot_map


def test_priority_queue():
    heap = MaxHeap()

    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(1)

    print("Priority queue:", heap.heap)
    print("Dispatching highest priority package:", heap.extract_max())
    print("Queue after dispatch:", heap.heap)


def main():
    graph = load_graph("data/network.txt")
    trie = build_trie_from_graph(graph)
    depot_map = build_depot_map(graph)


    while True:
        print("\n==== Smart Network Logistics Engine ====")
        print("1. Display network graph")
        print("2. Find shortest path distances from a node")
        print("3. Check for cycles")
        print("4. Test priority dispatch queue")
        print("5. Search node names by prefix")
        print("6. Look up a node")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nNetwork graph:")
            graph.display()

        elif choice == "2":
            start = input("Enter start node: ").strip().upper()
            end = input("Enter destination node: ").strip().upper()

            if start not in graph.graph or end not in graph.graph:
                print("Invalid node")
            else:
                distances, previous = dijkstra(graph, start)
                path = get_path(previous, start, end)

                if path:
                    print("\nShortest path:", " -> ".join(path))
                    print("Total cost:", distances[end])
                else:
                    print("No path found")

        elif choice == "3":
            if has_cycle(graph):
                print("\nCycle detected in the network")
            else:
                print("\nNo cycle in the network")

        elif choice == "4":
            test_priority_queue()

        elif choice == "5":
            prefix = input("Enter prefix: ").strip().upper()
            results = trie.search_prefix(prefix)

            if results:
                print("Matches:", results)
            else:
                print("No matches found")

        elif choice == "6":
            name = input("Enter node name: ").strip().upper()
            print(depot_map.get_depot(name))

        elif choice == "7":
            print("Exiting program")
            break

        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()

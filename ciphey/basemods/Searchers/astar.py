from collections import deque


class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        """
        adjacency list: basically the graph
        """
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {"A": 1, "B": 1, "C": 1, "D": 1}

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # TODO store the graph as an attribute
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            print(f"The open list is {open_list}")
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                print(f"The for loop node v is {v}")
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
                    print(f"The value of n is {n}")

            if n == None:
                print("Path does not exist!")
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                print("n is the stop node, we are stopping!")
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print("Path found: {}".format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            print(f"Self.neighbors is {self.get_neighbors(n)}")
            # for node in self.get_neighbors(n):
            #     print(f"And the iteration is {node, node.weight}")
            #     # if the current node isn't in both open_list and closed_list
            #     # add it to open_list and note n as it's parent
            #     if node not in open_list and node not in closed_list:
            #         open_list.add(node)
            #         parents[node] = n
            #         g[node] = g[n] + node.weight
            #     else:
            #         if g[node] > g[n] + node.weight:
            #             g[node] = g[n] + node.weight
            #             parents[node] = n

            #             if node in closed_list:
            #                 closed_list.remove(node)
            #                 open_list.add(node)

            for (m, weight) in self.get_neighbors(n):
                print(f"And the iteration is (m, weight)")
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            # open_list.remove(node)
            # closed_list.add(node)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None


class Node:
    """
    A node has a value assiocated with it
    Calculated from the heuristic
    """

    def __init__(self, h: float, edges: list):
        self.weight = h
        # Edges is a list of other nodes it can connect to
        self.edges = edges

    def __le__(self, node2):
        # if self is less than other
        return self.x <= node2.x

    def __lt__(self, node2):
        return self.x < node2.x

    def append_edge(self, edge):
        self.edges.append(edge)


adjacency_list = {
    "A": [("B", 1), ("C", 3), ("D", 7)],
    "B": [("D", 5)],
    "C": [("D", 12)],
}
A = Node(1, None)
B = Node(1, [A])
C = Node(3, [A, B])
D = Node(7, [C, B])

adjacency_list = {
    "A": [("B", 1), ("C", 3), ("D", 7)],
    "B": [("D", 5)],
    "C": [("D", 12)],
}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm("A", "D")

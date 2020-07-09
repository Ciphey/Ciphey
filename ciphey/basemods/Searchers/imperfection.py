import heapq


class Imperfection:
    """The graph is a Node: [List of nodes]
    Where each item in the list of nodes can also have a node with a list of nodes

    Ths result is that we can keep track of edges, while also keeping it small

    To calculate current, we push the entire graph to A*

    And it calculates the next node to choose, as well as increasing the size 
    of the graph with values

    We're using a heap, meaing the element at [0] is always the smallest element

    So we choose that and return it.


    The current A* implemnentation has an end, we simply do not let it end as LC will make it 
    end far before itreaches Searcher again.

    Current is the start position, so if we say we always start at the start of the graph it'll
    go through the entire graph

    graph = {
            Node: [
                {Node : 
                {
                    node
                    }
                }
                ]
            } 

    For encodings we just do them straight out

    The last value of parents from abstract 
    """

    """

   graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}"""

    def __init__(self):
        None

    def findBestNode(nodes):
        """Finds the best decryption module"""
        return next(iter(nodes))

    # def aStar(self, graph, current, end):
    #     """The A* search algorithm

    #     We're using heaps to find the minimum element (the one that will be the next current)
    #     Heaps are like sets with O(1) lookup time, but maintain the lowest element as [0]
    #     Sets insert in O(1), heaps in O(log N).

    #     https://stackoverflow.com/questions/4159331/python-speed-up-an-a-star-pathfinding-algorithm

    #     Current appears to be the list of all new tiles we can reach from current location

    #     End is the end node, that won't actually run bc LC will make it return before it hits aSTar function
    #     so tbh I'll just make it infinitite unless something else forces a return

    #     The graph is the actual data structure used. According to StackOvervlow, it looks like this:

    #     graph = {'A': ['B', 'C'],
    #              'B': ['C', 'D'],
    #              'C': ['D'],
    #              'D': ['C'],
    #              'E': ['F'],
    #              'F': ['C']}

    #     """

    #     # Runs decodings first

    #     openSet = set()
    #     openHeap = []
    #     closedSet = set()

    #     def retracePath(c):
    #         # Retraces a path back to the start
    #         path = [c]
    #         while c.parent is not None:
    #             c = c.parent
    #             path.append(c)
    #         path.reverse()
    #         return path

    #     # Adds the current location (start) to the heap and set
    #     openSet.add(current)
    #     openHeap.append((0, current))

    #     # while openSet contains items
    #     while openSet:
    #         # TODO change openSet  to a heap?
    #         # gets the 2nd element from the first element of the heap
    #         # so the heap is (0, current)
    #         # which means we pop current
    #         # this makes me think that current isn't the first?
    #         current = heapq.heappop(openHeap)[1]
    #         # We don't actually want to end, so I'm commenting this:
    #         # XXX
    #         if current == end:
    #             return retracePath(current)
    #         # Removes it from todo and into done i think
    #         # closedSet appears to be the set of things we have done
    #         openSet.remove(current)
    #         closedSet.add(current)

    #         """
    #         Okay so our graph looks like this:
    #         graph = {
    #                 Node: [
    #                     {Node :
    #                     {
    #                         node
    #                         }
    #                     }
    #                     ]
    #                 }
    #         graph[current] **SHOULD** be the list of nodes which contains dictionaries of nodes

    #         """
    #         for tile in graph[current]:
    #             # ClosedSet appears to be the list of visited nodes
    #             # TODO place this as a class attribute
    #             if tile not in closedSet:
    #                 # This is the heuristic
    #                 # TODO expected_time/probability + k * heuristic, for some experimentally determined value of k
    #                 tile.H = (abs(end.x - tile.x) + abs(end.y - tile.y)) * 10

    #                 # if tile is not in the openSet, add it and then pop it from the heap
    #                 if tile not in openSet:
    #                     openSet.add(tile)
    #                     heapq.heappush(openHeap, (tile.H, tile))
    #                 #  I have no idea where this code is called lol
    #                 tile.parent = current

    #     # This returns Nothing
    #     # I need to modify it so it finds the best item from Current
    #     # So basically, return item 0 of openHeap
    #     # return openHeap[0]
    #     # Since the [0] item is always minimum
    #     return []
    def aStar(self, graph, current, end):
        print(f"The graph is {graph}\nCurrent is {current}\n and End is {end}")
        openSet = set()
        openHeap = []
        closedSet = set()

        def retracePath(c):
            print("Calling retrace path")
            path = [c]
            while c.parent is not None:
                c = c.parent
                path.append(c)
            path.reverse()
            return path

        print("\n")

        openSet.add(current)
        openHeap.append((0, current))
        while openSet:
            print(f"Openset is {openSet}")
            print(f"OpenHeap is {openHeap}")
            print(f"ClosedSet is {closedSet}")
            print(f"Current is {current}")
            print(f"I am popping {openHeap} with the first element")
            current = heapq.heappop(openHeap)[1]
            print(f"Current is now {current}")
            print(f"Graph current is {graph[current]}")
            if current == end:
                return retracePath(current)
            openSet.remove(current)
            closedSet.add(current)
            for tile in graph[current]:
                if tile not in closedSet:
                    tile.H = (abs(end.x - tile.x) + abs(end.y - tile.y)) * 10
                    tile.H = 1
                    if tile not in openSet:
                        openSet.add(tile)
                        heapq.heappush(openHeap, (tile.H, tile))
                    tile.parent = current
            print("\n")
        return []


class Node:
    """
    A node has a value assiocated with it
    Calculated from the heuristic
    """

    def __init__(self, h):
        self.h = h
        self.x = self.h
        self.y = 0.6

    def __le__(self, node2):
        # if self is less than other
        return self.x <= node2.x

    def __lt__(self, node2):
        return self.x < node2.x


if __name__ == "__main__":
    obj = Imperfection()
    graph = {
        "A": ["B", "C"],
        "B": ["C", "D"],
        "C": ["D"],
        "D": ["C"],
        "E": ["F"],
        "F": ["C"],
    }
    # Makes the graph
    y = Node(0.5)
    x = Node(0.3)
    p = Node(0.7)
    q = Node(0.9)
    graph = {y: [x, p], p: q}

    print(obj.aStar(graph, y, q))

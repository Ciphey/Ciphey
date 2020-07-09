function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.prepend(current)
    return total_path

// A* finds a path from start to goal.
// h is the heuristic function. h(n) estimates the cost to reach goal from node n.
function A_Star(graph, start, h)
    // The set of discovered nodes that may need to be (re-)expanded.
    // Initially, only the start node is known.
    // This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet := {start}

    // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    // to n currently known.
    cameFrom := an empty map

    // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore := map with default value of Infinity
    gScore[start] := 0

    // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    // how short a path from start to finish can be if it goes through n.
    fScore := map with default value of Infinity
    fScore[start] := h(start)
    
    // the exit condition is set to True when LC returns True
    exit_condition = False

    while not exit_condition
        // This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current := the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for each neighbor of current
		decodings = neighbor.decoders()
		
	
	
            // d(current,neighbor) is the weight of the edge from current to neighbor
            // tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore := gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]
                // This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] := current
                gScore[neighbor] := tentative_gScore
                fScore[neighbor] := gScore[neighbor] + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)
		
		    # run the cracker on the object
			    crack(node.ctext)
		    if crack:
			    # if cracker returns true, reconstruct path and exiti
			    exit_condition = True
			    reconstruct(start, node)
		    else:
			    # else add the new children of the cracker to openSet
			    openSet.append(node: crack)
		
		
		

    // Open set is empty but goal was never reached
    return failure
    

function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.prepend(current)
    return total_path

// A* finds a path from start to goal.
// h is the heuristic function. h(n) estimates the cost to reach goal from node n.
function A_Star(graph, start, h)
    // The set of discovered nodes that may need to be (re-)expanded.
    // Initially, only the start node is known.
    // This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet := {start}

    // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    // to n currently known.
    cameFrom := an empty map

    // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore := map with default value of Infinity
    gScore[start] := 0

    // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    // how short a path from start to finish can be if it goes through n.
    fScore := map with default value of Infinity
    fScore[start] := h(start)
    
    // the exit condition is set to True when LC returns True
    exit_condition = False

    while not exit_condition
        // This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current := the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for each neighbor of current
		decodings = neighbor.decoders()
		
	
	
            // d(current,neighbor) is the weight of the edge from current to neighbor
            // tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore := gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]
                // This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] := current
                gScore[neighbor] := tentative_gScore
                fScore[neighbor] := gScore[neighbor] + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)
		
		    # run the cracker on the object
			    crack(node.ctext)
		    if crack:
			    # if cracker returns true, reconstruct path and exiti
			    exit_condition = True
			    reconstruct(start, node)
		    else:
			    # else add the new children of the cracker to openSet
			    openSet.append(node: crack)
		
		
		

    // Open set is empty but goal was never reached
    
function calculate_new_children(node):

    
class Node:
    """
    A node has a value assiocated with it
    Calculated from the heuristic
    """

    def __init__(self, h: float = None, edges: (any, float) = None, ctext: str = None):
        self.weight = h
        # Edges is a list of other nodes it can connect to
        self.edges = edges
        self.ctext = ctext
        self.h = h
        self.path = []
        self.information_content = config.cache.get_or_update(
            self.ctext,
            "cipheycore::info_content",
            lambda: cipheycore.info_content(self.ctext),
        )

    def __le__(self, node2):
        # if self is less than other
        return self.x <= node2.x

    def __lt__(self, node2):
        return self.x < node2.x

    def append_edge(self, edge):
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

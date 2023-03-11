# depth-first search (DSF) is an algorithm used to traverse
# or locate a targe node in a graph or tree data structure

# goes as far as it possibly can go until it has to backtrack
# DFS is widely-used as part of many algorithms that resolve
# graph-represented problems

# Functionality:
#  - 1. Mark the current node as visited
#  - 2. Traverse the neighboring nodes that aren't visited
#       and recursively call the DFs function for that node


# we can mark the nodes as visited so we don't have to enter an infinite loop


class Graph:
    # defines a constructor
    def __init__(self, num_of_nodes, directed):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Directed or Undirected
        self.m_directed = directed

        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}

        # Add edge to the graph

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])


    def dfs(self, start, target, path=[], visited=set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for (neighbour, weight) in self.m_adj_list[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None


graph = Graph(5, directed=False)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_adj_list()

traversal_path = []
traversal_path = graph.dfs(0, 3)
print(traversal_path)
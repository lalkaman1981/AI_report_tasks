'''Working with graphs'''

from memory_profiler import profile
import time

# @profile
def get_graph_from_file(file_name: str) -> list:
    """ 
    (str) -> (list)
    
    Read graph from file and return a list of edges.
    
    >>> import tempfile
    >>> sample = '1,2\\n3,4\\n1,5'
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as tmpfile:
    ...     _ = tmpfile.write(sample)
    ...     _ = tmpfile.flush()
    ...     get_graph_from_file(tmpfile.name)
    [[1, 2], [3, 4], [1, 5]]

    """
    graph = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            node1, node2 = map(int, line.strip().split(','))
            graph.append([node1, node2])
    return graph

def to_edge_dict(edge_list: list) -> dict:
    """ 
    (list) -> (dict)

    Convert a graph from list of 
    edges to dictionary of vertices.
    
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [3, 2], 5: [1]}
    """
    dictionary = {}
    for edge in edge_list:
        for node in edge:
            if node not in dictionary:
                dictionary[node] = []
            dictionary[node].append(edge[1 - edge.index(node)])
    return dictionary


def is_edge_in_graph(graph: dict, edge: tuple) -> bool:
    """ 
    (dict, tuple) -> bool
    
    Return True if graph contains a given edge 
    and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4],\
          3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    for i in graph.keys():
        for j in graph[i]:
            o = tuple([i, j])
            if edge == o:
                return True
    return False



def add_edge(graph: dict, edge: tuple) -> dict:
    """ 
    (dict, tuple) -> dict
    
    Add a new edge to the graph and return new graph. 
    
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 6))
    {1: [2, 5, 6], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1], 6: [1]}
   
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
     
    """

    for node in edge:
        if node not in graph:
            graph[node] = []  # Create the node if it doesn't exist
        graph[node].append(edge[1 - edge.index(node)])  # Add the opposite node

    return graph


def del_edge(graph: dict, edge: tuple) -> dict:
    """ 
    (dict, tuple) -> (dict)
    
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 4))
    {1: [2, 5], 2: [1, 4], 4: [2], 5: [1]}
    """
    for node in edge:
        if node in graph:  # Only check for nodes that exist
            neighbors = graph[node]
            try:
                neighbors.remove(edge[1 - edge.index(node)])  # Remove opposite node
                if not neighbors:  # Delete node if no neighbors remain
                    del graph[node]
            except ValueError:
                pass  # Edge didn't exist, that's okay

    return graph


def add_node(graph: dict, node: int) -> dict:
    """ 
    (dict, int) -> (dict)
    
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    >>> add_node({1: [2], 2: [1]}, 1)
    {1: [2], 2: [1]}
    """
    if node not in graph:
        graph[node] = []
    return graph

def del_node(graph: dict, node: int) -> dict:
    """ 
    (dict, int) -> (dict)
    
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    graph.pop(node, None)  # Safely delete the node

    # Iterate over neighbor lists, removing references to the deleted node
    for neighbor_list in graph.values():
        try:
            neighbor_list.remove(node)
        except ValueError:
            pass  # Node was not a neighbor, that's okay

    return graph

def convert_to_dot(filename:str) -> None:
    """
    Get graph from a file and save the directed graph to a file in a DOT format with the same name.
    
    >>> import tempfile
    >>> sample = '1,2\\n3,4\\n1,5'
    >>> test_result = 'digraph {\\n1 -> 2\\n1 -> 5\\n2 -> 1\\n3 -> 4\\n4 -> 3\\n5 -> 1\\n}'
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as tmpfile:
    ...     _ = tmpfile.write(sample)
    ...     _ = tmpfile.flush()
    ...     convert_to_dot(tmpfile.name)
    ...     fl = tmpfile.name.split('.')[0] + '.dot'
    >>> with open (fl, 'r') as dot_file:
    ...     test_result == dot_file.read()
    True
    """
    g = get_graph_from_file(filename)
    dct = to_edge_dict(g)
    pairs = []
    for key, _ in dct.items():
        for i in dct[key]:
            pair = [key, i]
            pairs.append(pair)

    dotted = filename.split('.')[0] + '.dot'
    with open(dotted, 'w', encoding= 'utf-8') as file:
        file.write("digraph {\n")
        for edge in pairs:
            file.write(f'{edge[0]} -> {edge[1]}\n')
        file.write("}")

if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    ...

start_time = time.time()
convert_to_dot('big_test.txt')
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
Time taken: 0.017834186553955078 seconds
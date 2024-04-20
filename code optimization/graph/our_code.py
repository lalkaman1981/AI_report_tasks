'''Working with graphs'''

from memory_profiler import profile


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
    with open(file_name, 'r', encoding='utf-8') as file:
        coordinates = file.readlines()
        graph = []
        for line in coordinates:
            coord = []
            line = line.split(',')
            coord.append(int(line[0]))
            coord.append(int(line[1]))
            graph.append(coord)
        return graph

def to_edge_dict(edge_list: list) -> dict:
    """ 
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.
    
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    dictionary = {}
    lst = []
    for i in edge_list:
        for j in i:
            lst.append(j)

    lst = list(set(lst))
    for i in lst:
        value = []
        for n in edge_list:
            if i in n:
                if n[0]==i:
                    value.append(n[1])
                if n[1]==i:
                    value.append(n[0])
        value = sorted(value)
        dictionary[i] = value

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

    for j in edge:
        if j in graph.keys():
            if j == edge[0]:
                graph[j] = graph[j] + [edge[1]]
            if j == edge[1]:
                graph[j] = graph[j] + [edge[0]]
        else:
            if j == edge[0]:
                graph[j] = [edge[1]]
            if j == edge[1]:
                graph[j] = [edge[0]]
            continue
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
    for i in edge:
        if i in graph.keys():
            lst = graph[i]
            if edge[0] in lst or edge[1] in lst:
                if i == edge[0]:
                    lst.remove(edge[1])
                if i == edge[1]:
                    lst.remove(edge[0])

                if lst == []:
                    del graph[i]
                else:
                    graph[i] = lst

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
    if node not in graph.keys():
        graph[node] = []
    return graph

def del_node(graph: dict, node: int) -> dict:
    """ 
    (dict, int) -> (dict)
    
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph.keys():
        del graph[node]
    for i in graph.values():
        if node in i:
            i.remove(node)

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

convert_to_dot('big_test.txt')

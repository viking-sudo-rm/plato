from src.graph_family import GraphFamily
from src.serialized_graph import SerializedGraph, SerializedGraphNode

# TODO: Build backward, output structured graph?


def serialize(graph_family: GraphFamily, n: int):
    nodes = []
    i = 0
    while True:
        node_type = graph_family.get_node_type(n, i)
        if node_type is None:
            break
        # TODO: Make more efficient than n^2!
        # Can do this by binary se
        args = [] 
        for j in range(i):
            conn = graph_family.get_connection(n, i, j)
            if conn != -1:
                args.append((conn, j))
        args.sort()
        args = [arg[1] for arg in args]
        node = SerializedGraphNode(node_type, args)
        nodes.append(node)
        i += 1
    
    return SerializedGraph(nodes)

from typing import NamedTuple


class SerializedGraphNode(NamedTuple):
    callback: callable
    arguments: list

    def __repr__(self):
        return f"{self.callback.__name__}({','.join(self.arguments)})"


class SerializedGraph:

    def __init__(self, nodes):
        self.nodes = nodes
    
    def __call__(self, inputs):
        values = [None for _ in self.nodes]
        for idx, node in enumerate(self.nodes):
            if len(node.arguments) == 0:
                values[idx] = node.callback(inputs)
            else:
                arg_values = [values[ptr] for ptr in node.arguments]
                values[idx] = node.callback(arg_values)
        return values

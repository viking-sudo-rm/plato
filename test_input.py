from unittest import TestCase

from src.lib.input import InputGraphFamily
from src.serialize import serialize


input_graph_family = InputGraphFamily()

graph = serialize(input_graph_family, 5)
print("Graph", graph.nodes)
inputs = [0, 1, 2, 3, 4]
print("Input", inputs)
outputs = graph([0, 1, 2, 3, 4])
print("Output", outputs)

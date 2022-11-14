from unittest import TestCase

from src.lib.input import InputGraphFamily
from src.serialize import serialize


class TestInput(TestCase):

    def test_input(self):
        input_graph_family = InputGraphFamily()
        graph = serialize(input_graph_family, 5)
        inputs = [0, 1, 2, 3, 4]
        outputs = graph([0, 1, 2, 3, 4])
        self.assertEqual(outputs, inputs)

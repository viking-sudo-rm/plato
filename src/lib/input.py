from src.graph_family import GraphFamily


def make_projection(idx: int) -> callable:
    def project(inputs):
        return inputs[idx]
    return project


class InputGraphFamily:

    def get_node_type(self, n: int, i: int) -> callable:
        if i >= n:
            return None
        return make_projection(i)

    def get_connection(self, n: int, i: int, j: int) -> int:
        return -1

    def __repr__(self):
        return "input()"
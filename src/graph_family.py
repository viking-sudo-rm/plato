from abc import ABCMeta, abstractmethod


class GraphFamily(metaclass=ABCMeta):

    @abstractmethod
    def get_node_type(self, n: int, i: int) -> callable:
        return NotImplemented

    @abstractmethod
    def get_connection(self, n: int, i: int, j: int) -> int:
        return NotImplemented

from .edge import Edge


# Possible status  START, END
class Node:
    """This class represent node in FSA"""
    edges: list[Edge]
    name: str
    language: set[str]
    contains: set[str]
    index: int
    dirs: dict[str, str]
    status: str

    def __init__(self,
                 name: str,
                 index: int,
                 lang: set[str]):
        self.name = name
        self.index = index
        self.language = lang
        self.contains = set()
        self.edges = []
        self.dirs = {}
        self.status = "NONE"

    def add_edge(self, edge: Edge):
        self.contains |= edge.contains
        self.edges += [edge]
        for letter in edge.contains:
            self.dirs[letter] = edge.tail

    def get(self, letter: str):
        return self.dirs.get(letter)

    @property
    def isComplete(self) -> bool:
        return self.contains == self.language

    def __repr__(self) -> str:
        return f'<Node[{self.name}] -> {self.edges}>'

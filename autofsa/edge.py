class Edge:
    """ This class represent edge between nodes in FSA"""
    tail_name: str
    head_name: str
    contains: set[str]

    def __init__(self,
                 head: str,
                 tail: str,
                 contains: set[str]):
        self.head = head
        self.tail = tail
        self.contains = contains

    @property
    def label(self):
        return '{' + ','.join(self.contains) + '}'

    def __repr__(self) -> str:
        return f"<Edge [{self.head}]->[{self.tail}] {self.label}>"

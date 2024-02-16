from typing import Iterator

from .node import Node
from .edge import Edge
import graphviz
from itertools import product

from .render_config import GRAPH_PARAMS, DEFAULT_NODE, START_NODE, END_NODE


class INDEX:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        self.a += 1
        return self.a


class FSA:
    """This class present Finite State Automate"""
    name: str
    nodes: list[Node]
    edges: list[Edge]
    language: set[str]
    sub_name: str
    index: INDEX
    NODES: Iterator[int]
    start: Node | None
    end_nodes: list[Node]
    dct: dict[str, Node]

    def __init__(self,
                 name: str,
                 language: set[str],
                 sub_name: str = None,
                 ):
        self.name = name
        self.letter = sub_name
        self.language = language
        self.sub_name = sub_name
        self.NODES = iter(INDEX())
        self.nodes = []
        self.edges = []
        self.dct = {}
        self.start = None
        self.end_nodes = []

    def create_node(self) -> Node:
        """ Will create node and add it into fsa if sub name is exist """
        assert self.sub_name, "Sub_name is need to be specified!"
        node_index = next(self.NODES)

        node_name = f"{self.sub_name}{node_index}"
        node = Node(name=node_name,
                    index=node_index,
                    lang=self.language)
        self.nodes += [node]
        self.dct[node.name] = node
        return node

    def add_ends(self, *ends):
        for _ in ends: _.status = "END"
        self.end_nodes += ends

    def set_start(self, node: Node):
        assert self.start is None, "You specifying FSA's start node twice!"
        node.status = "START"
        self.start = node

    def add_node(self, name):
        node_index = next(self.NODES)
        node = Node(name=name,
                    index=node_index,
                    lang=self.language)
        self.nodes += [node]
        self.dct[node.name] = node
        return node

    def edge_between(self,
                     head: Node,
                     tail: Node,
                     contains: set[str]) -> Edge:
        if tail not in head.dirs.values():
            edge = Edge(head=head.name, tail=tail.name, contains=contains)
            self.nodes[head.index - 1].add_edge(edge)
            self.edges += [edge]
            return edge
        else:
            for edge in head.edges:
                if edge.tail == tail.name:
                    edge.contains |= contains
                    return edge

    def edge_between_names(self,
                           head: str,
                           tail: str,
                           contains: set[str]) -> Edge:
        return self.edge_between(self.dct[head], self.dct[tail], contains)

    @property
    def isComplete(self) -> bool:
        return all([n.isComplete for n in self.nodes])

    def render(self,
               folder: str = None,
               output_format: str = 'jpg'):
        assert self.start is not None, "Start node must be set in FSA!"
        assert len(self.end_nodes) != 0, "No end nodes provided in FSA!"

        dot = graphviz.Digraph(comment=self.name, graph_attr=GRAPH_PARAMS)
        [dot.node(node.name, node.name, DEFAULT_NODE) for node in self.nodes if node.status == 'NONE']
        [dot.node(node.name, node.name, START_NODE) for node in self.nodes if node.status == 'START']
        [dot.node(node.name, node.name, END_NODE) for node in self.nodes if node.status == 'END']

        [dot.edge(edge.head, edge.tail, label=edge.label) for edge in self.edges]
        path = f'{"output" if not folder else folder}/{self.name}'
        dot.render(path,
                   format=output_format).replace('\\', '/')

        print(f"{self.name}.{output_format} Was successfully generated! path:{path}")

    def get_node(self, name: str) -> Node | None:
        """ Get node by name"""
        return self.dct.get(name)

    def operate(self, other, operation: str):
        assert self.isComplete, "To perform operations on FSA's they should be complete!"
        assert other.isComplete, "To perform operations on FSA's they should be complete!"
        assert self.language == other.language, "To perform operations on FSA's they should have equal language!"
        OPERATIONS = {
            "or": lambda x, y: x | y,
            "and": lambda x, y: x & y,
        }
        assert operation in OPERATIONS.keys(), "This operation don't supported!"

        new_fsa = FSA(f'[{self.name}]{operation}[{other.name}]', self.language)
        for n1 in self.nodes:
            for n2 in other.nodes:
                name1 = n1.name
                name2 = n2.name
                new_name = name1 + name2
                new_fsa.add_node(new_name)
        for n1 in self.nodes:
            for n2 in other.nodes:
                node = n1.name + n2.name
                for letter in self.language:
                    to = n1.get(letter) + n2.get(letter)
                    new_fsa.edge_between_names(node, to, {letter})

        new_start_node = new_fsa.get_node(self.start.name + other.start.name)
        new_fsa.set_start(new_start_node)
        for n1 in self.nodes:
            for n2 in other.nodes:
                node = new_fsa.get_node(n1.name + n2.name)
                if OPERATIONS[operation](n1 in self.end_nodes, n2 in other.end_nodes):
                    new_fsa.add_ends(node)
        return new_fsa

    def trace(self, sentence: str) -> bool:
        curr = self.start
        p = 0
        while p < len(sentence):
            l = sentence[p]
            next_node = self.get_node(curr.dirs[l])
            curr = next_node
            p += 1
        return curr.status == "END"

    def verify(self,
               func,  # sentence -> bool if it is correct
               max_depth,
               min_depth: int = 1,
               ) -> None:
        assert self.isComplete, "To perform verification of FSA should be complete!"
        assert self.start is not None, "Start node must be set in FSA!"
        assert len(self.end_nodes) != 0, "No end nodes provided in FSA!"
        verification_lang = self.language
        tests, tests_failed = 0, 0
        verified = True
        for sub_depth in range(min_depth, max_depth + 1):
            for sentence in product(verification_lang, repeat=sub_depth):
                sentence = ''.join(sentence)
                if self.trace(sentence) != func(sentence):
                    fsa_ans = 'V' if self.trace(sentence) else 'X'
                    func_ans = 'V' if func(sentence) else 'X'
                    print(f"FSA Wrong Answer! testcase: {sentence} -> FSA: {fsa_ans}, FUNC:{func_ans}")
                    verified = False
                    tests_failed += 1
                tests += 1
        if verified:
            print(f"{self.name} was successfully verified {tests_failed}/{tests} tests were failed!")
        else:
            print(f"Verification of {self.name} was not successful {tests_failed}/{tests} tests were failed!")

    def make_complete(self, trash):
        for node in self.nodes:
            self.edge_between(node, trash, self.language - node.contains)

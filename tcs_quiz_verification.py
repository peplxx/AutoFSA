from autofsa.fsa import FSA


def check_divisible(string: str):
    return int(string, 2) % 3 == 0


def check_divisible_inverted(string: str):
    return int(string[::-1], 2) % 3 == 0


fsa = FSA("quiz", {'1', '0'}, 'a')
q0 = fsa.create_node()
fsa.set_start(q0)

q1 = fsa.create_node()
q2 = fsa.create_node()
fsa.edge_between(q0, q0, {'0'})
fsa.edge_between(q0, q1, {'1'})
fsa.edge_between(q1, q0, {'1'})
fsa.edge_between(q1, q2, {'0'})
fsa.edge_between(q2, q1, {'0'})
fsa.edge_between(q2, q2, {'1'})
fsa.add_ends(q0)

fsa.verify(check_divisible, max_depth=7)

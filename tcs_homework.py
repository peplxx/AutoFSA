from autofsa.fsa import FSA
from collections import Counter

fsa = FSA("even_letters", {'a', 'b'}, sub_name='p')
p00 = fsa.create_node()

p10 = fsa.create_node()
p01 = fsa.create_node()
p11 = fsa.create_node()

fsa.edge_between(p00, p10, {'a'})
fsa.edge_between(p00, p01, {'b'})

fsa.edge_between(p10, p00, {'a'})
fsa.edge_between(p10, p11, {'b'})

fsa.edge_between(p01, p00, {'b'})
fsa.edge_between(p01, p11, {'a'})

fsa.edge_between(p11, p10, {'b'})
fsa.edge_between(p11, p01, {'a'})
fsa.add_ends(p00)
fsa.set_start(p00)
fsa.verify(lambda x: all([i % 2 == 0 for i in Counter(x).values()]), max_depth=6)
fsa.render()

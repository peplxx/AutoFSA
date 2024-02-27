from autofsa import FSA

fsa = FSA(name='fsa1',
          sub_name='q',
          language={'0', '1'})
q1 = fsa.create_node()
fsa.set_start(q1)
q2 = fsa.create_node()
fsa.edge_between(q1, q1, {'0'})
fsa.edge_between(q1, q2, {'1'})
fsa.edge_between(q2, q1, {'1'})
fsa.edge_between(q2, q2, {'0'})
fsa.add_ends(q2)
fsa.render()

fsa2 = FSA(name='fsa2',
           sub_name='p',
           language={'0', '1'})
p1 = fsa2.create_node()
fsa2.set_start(p1)
p2 = fsa2.create_node()
fsa2.edge_between(p1, p1, {'1'})
fsa2.edge_between(p1, p2, {'0'})
fsa2.edge_between(p2, p1, {'0'})
fsa2.edge_between(p2, p2, {'1'})
fsa2.add_ends(p2)
fsa2.render()

f12 = fsa.operate(fsa2, operation="or")
f12.render()


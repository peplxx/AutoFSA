from autofsa.fsa import FSA

lang = {"w", "t", 'a', 'l', 'k', 'e', 'd'}

fsa = FSA(language=lang, sub_name='t', name='WordsFSA')

q1 = fsa.create_node()
fsa.set_start(q1)
q2 = fsa.create_node()
q3 = fsa.create_node()
q4 = fsa.create_node()
q5 = fsa.create_node()
q6 = fsa.create_node()
q7 = fsa.create_node()
trash = fsa.create_node()
fsa.edge_between(q1, q2, {'w', 't'})
fsa.edge_between(q2, q3, {'a'})
fsa.edge_between(q3, q4, {'l'})
fsa.edge_between(q4, q5, {'k'})
fsa.edge_between(q5, q6, {'e'})
fsa.edge_between(q6, q7, {'d'})

fsa.make_complete(trash)
fsa.add_ends(q7)

fsa.verify(lambda x:x == 'walked' or x == 'talked',max_depth=6)
fsa.render()
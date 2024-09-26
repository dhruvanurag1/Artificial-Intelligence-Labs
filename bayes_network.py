from pomegranate import *

Cancer = DiscreteDistribution({'cancer':0.01, 'no-cancer': 0.99})

Tester = ConditionalProbabilityTable([['cancer', 'positive', 0.9], 
['cancer', 'negative', 0.1], 
['no-cancer', 'positive', 0.2], 
['no-cancer', 'negative', 0.8]], [Cancer])

s_cancer = State(Cancer, 'disease')
s_tester_1 = State(Tester, 'tester_1')
s_tester_2 = State(Tester, 'tester_2')

modela = BayesianNetwork('disease')

modela.add_states(s_cancer, s_tester_1, s_tester_2)

modela.add_transition(s_cancer, s_tester_1)
modela.add_transition(s_cancer, s_tester_2)

modela.bake()

print ('The number of nodes:', modela.node_count())
print ('The number of edges:', modela.edge_count())

print(modela.predict_proba({'tester_1':'positive', 'tester_2' : 'positive'})[0].parameters)

print(modela.predict_proba({'tester_1':'positive', 'tester_2' : 'negative'})[0].parameters)

print(modela.predict_proba({'tester_1':'positive'})[2].parameters)

from pomegranate import *

graduation = DiscreteDistribution({'graduate':0.9, 'not-graduate': 0.1})

job_1 = ConditionalProbabilityTable([['graduate', 'O1', 0.5], 
['graduate', 'not-O1', 0.5],
['not-graduate', 'O1', 0.05],
['not-graduate', 'not-O1', 0.95]], [graduation])

job_2 = ConditionalProbabilityTable([['graduate', 'O2', 0.75],
['graduate', 'not-O2', 0.25], 
['not-graduate', 'O2', 0.25],
['not-graduate', 'not-O2', 0.75]], [graduation])

s1 = State(graduation, 'graduation')
s2 = State(job_1, 'o1')
s3 = State(job_2, 'o2')

model = BayesianNetwork('graduation')

model.add_states(s1, s2, s3)

model.add_transition(s1, s2)
model.add_transition(s1, s3)

model.bake()

print ('The number of nodes:', model.node_count())
print ('The number of edges:', model.edge_count())



print('a', model.predict_proba({'graduation':'graduate', 'o1' : 'not-O2'})[2].parameters)
print('b', model.predict_proba({'o1':'O1', 'o2':'O2'})[0].parameters)
print('c', model.predict_proba({'o1':'not-O1', 'o2':'O2'})[0].parameters)
print('d', model.predict_proba({'o1':'not-O1', 'o2':'not-O2'})[0].parameters)
print('e',model.predict_proba({'o1':'O1'})[2].parameters)


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

print('a', modela.predict_proba({'tester_1':'positive', 'tester_2' : 'positive'})[0].parameters)

print('b', modela.predict_proba({'tester_1':'positive', 'tester_2' : 'negative'})[0].parameters)

print('d', modela.predict_proba({'tester_1':'positive'})[2].parameters)

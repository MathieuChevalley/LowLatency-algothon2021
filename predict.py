from sys import stdin
from sklearn.linear_model import LogisticRegression
import pickle

with open('model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)

# classify terminal input
for line in stdin:
    if line == '': 
        break
    d=[float(x) for x in line.split(',')]
    d = d[-2:]
    print(pickle_model.predict([d])[0])


from numpy import array
import numpy as np

good = eval(open('data/good.txt').read().strip())
bad = eval(open('data/bad.txt').read().strip())
x = array(good + bad) * 100
y = np.repeat(np.resize(array(len(good) * [1] + len(bad) * [0]), (x.shape[0], 1)), 20, axis=1)
arr = np.array([x, y])[:, np.random.permutation(x.shape[0]), :]
x = arr[0]
y = np.resize(arr[1][:, ::20], (x.shape[0],))

training = 40
testing = 40
assert training + testing < x.shape[0]

atraining = (x[:training], y[:training])
atesting = (x[-testing:], y[-testing:])

from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
scalar.fit(atraining[0])

atraining = (scalar.transform(atraining[0]), atraining[1])
atesting = (scalar.transform(atesting[0]), atesting[1])

from sklearn.neural_network import MLPClassifier
c = MLPClassifier(solver='lbfgs', alpha=1e-5,
    hidden_layer_sizes=(18, 12, 6, 3), random_state=1)
c = c.fit(*atraining)

percentage = np.sum(1 - np.abs(c.predict(atesting[0]) - atesting[1]))
percentage = percentage / testing * 100

from sen2vec import sen2vec
print(f'{round(percentage, 2)}% was classified correctly.')

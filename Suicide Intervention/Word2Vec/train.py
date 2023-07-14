
data = 'assets/text8.txt'
model = 'model/model.txt'

import word2vec
word2vec.word2vec(data, model, size=20, verbose=True)

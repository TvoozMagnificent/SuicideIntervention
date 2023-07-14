
# import heartrate; heartrate.trace(browser=True)

model = 'Word2Vec/model/model.txt'
clusters = 'Word2Vec/model/clusters.txt'

import word2vec
model = word2vec.load(model)
print('Model loaded')

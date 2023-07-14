import heartrate; heartrate.trace(browser=True)

model = 'model/model.txt'
clusters = 'model/clusters.txt'

import word2vec
model = word2vec.load(model)
print('Model loaded')

words = [_ for _ in model.vocab[1:][:2000] if len(_) > 2]
print('Words generated')
neighbors = {_: [x for x in model.vocab[model.similar(_)[0]] if x in words] for _ in words}
print('Neighbors generated')


model = 'Word2Vec/model/model.txt'
import word2vec
model = word2vec.load(model)
print('Model loaded')
import numpy as np

from translate import Translator
translator = Translator(from_lang='zh', to_lang="en")
translate = translator.translate

def filtered_translate(text):
    translation = translate(text)
    for character in "!@#$%^&*()~`1234567890-=_+[]\{}|;':\",./<>?\t\n":
        translation = translation.replace(character, ' ')
    while "  " in translation: translation = translation.replace('  ', ' ')
    return translation.lower().strip().split(' ')

def sen2vec(sentence):
    sum = np.zeros(20)
    for word in filtered_translate(sentence):
        try: sum += model[word]
        except KeyError: pass # stupid word
    return list(sum)

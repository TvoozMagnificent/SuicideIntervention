
from glob import glob
from functools import reduce

good = 'data/good/*'
bad = 'data/bad/*'

good_data = reduce(lambda x, y: x+y, [
    eval(open(_).read().strip()) for _ in glob(good)
])
bad_data = reduce(lambda x, y: x+y, [
    eval(open(_).read().strip()) for _ in glob(bad)
])

open('data/good.txt','w').write(str(good_data))
open('data/bad.txt','w').write(str(good_data))

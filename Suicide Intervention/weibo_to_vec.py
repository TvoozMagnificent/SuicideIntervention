
from os import mkdir
from sen2vec import sen2vec

users = [
    _.split(',', 1)[0].strip()
    for _ in open('weibo-crawler/weibo/users.csv').read().strip().split('\n')[1:]
]

for user in users:
    posts = [
        sen2vec(_.split(',', 3)[-2].strip())
        for _ in open(f'weibo-crawler/weibo/{user}/{user}.csv').read().strip().split('\n')[1:]
    ]

    open(f'data/good/{user}', 'w').write(str(posts))

# 参数收集的逆过程
def add(x, y):
    return x + y


params = (1, 2)
print(add(*params))  # 3


def with_star(**kwds):
    print(kwds['name']+kwds['age'])


def without_star(kwds):
    print(kwds['name']+kwds['age'])


args = {'name': 'ls', 'age': '24'}
with_star(**args)  # ls 24
without_star(args)  # ls 24

# 收集参数
def params(*params):
    print(params)


# * 收集其余的位置参数.如果不提供任何元素,params就是空的元组.
params()  # ()
params(1)  # (1,)
params([1, 2, 3])  # ([1, 2, 3],)
params({1, 2, 3})  # ({1, 2, 3},)


def params2(**params):
    print(params)


params2()  # {}
params2(x=1, y=2, z=3)  # {'x': 1, 'y': 2, 'z': 3}


def params3(*params1, **params2):
    print(params1)
    print(params2)


params3(1, 2, 3, x=1, y=2)  # (1, 2, 3) {'x': 1, 'y': 2}

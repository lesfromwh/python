# 关键字参数和默认值
def hello(greeting, name):
    print('%s %s' % (greeting, name))


hello('hello', 'world')
hello('world', 'hello')
# 在参数列表添加参数名,可以回避位置问题.
hello(name='world', greeting='hello')


# 定义函数的时候也可以在参数列表加上.
def hello2(greeting='hello', name='world2'):
    print('%s %s' % (greeting, name))


hello2()  # hello world2

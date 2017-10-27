# 作用域
def foo():
    x = 10


# 如果在函数内部将值赋给一个变量,他会默认成为局部变量.如果给全局变量赋值呢?用global即可.
def foo2():
    global x
    x = 20


x = 1
foo()  # 局部变量不影响全局变量
print(x)  # 1
foo2()
print(x)


def output(x):
    print(x + x)  # 如果局部变量或者参数名字和想要访问的全局变量的名字相同的话就不能直接访问了.


# globals()['xxx']
def output2(x):
    print(x + globals()['x'])


output(2)
output2(2)

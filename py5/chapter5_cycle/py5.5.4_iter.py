# 一些迭代工具
name = ['ls', 'wb', 'dfy', 'jm']
age = ['18', '25', '24', '17']
# print(range(4))  # range(0, 4)
for i in range(len(name)):
    print(name[i], 'is', age[i], 'years old')

# 内建zip函数 把两个序列压缩在一起.
print(zip(name, age))  # <zip object at 0x00000231680A73C8>  [(ls,18),(x,x),(x,x),(x,x)]
for name, age in zip(name, age):
    print(name, 'is', age)

# zip也可以作用余任意多的序列.它可以处理不等长的序列,当最短的序列'用完'的时候就会停止.
for x, y in zip(range(4), range(10)):  # 0 0 1 1 2 2 3 3
    print(x, y)

for index, s in enumerate(['a', 'b', 'c']):
    print(index, ',', s)
# 0 , a
# 1 , b
# 2 , c

# sorted 和 reversed
print(sorted([2, 5, 1, 6]))  # [1, 2, 5, 6]
iterator = reversed('hello')
print(iterator)
for x in reversed('hello'):
    print(x)

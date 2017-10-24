# 列表基本操作
# 1.改变列表
L = list('hello')
L[1] = 's'
print(L)  # ['h', 's', 'l', 'l', 'o']

# 2.删除元素
del L[4]
print(L)  # ['h', 's', 'l', 'l']

# 3.分片赋值
name = ['ls', 'tyl', 'zl', 'hd']
# 3.1.可以使用与原序列不等长的序列将分片替换.
name[2:] = list('tyl')
print(name)  # ['ls', 'tyl', 't', 'y', 'l']
# 3.2.分片赋值语句可以在不需要替换任何元素的情况下差人新的元素.
name2 = [1, 5]
name2[1:1] = [2, 3, 4]
print(name2)  # [1, 2, 3, 4, 5]

# 通过分片赋值来删除元素也是可以的.
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = []
print(numbers)  # [1, 5]

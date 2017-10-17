# 迭代
list = [1, 2, 3, 4, 5, 6, 7]
for x in list:
    print(x)

dic = {'a': '1', 'b': '2'}
for x in dic:
    print(x)
# 遍历value
for value in dic.values():
    print(value)
# 遍历key-value
for k, v in dic.items():
    print(k, v)

# 字符串也可以遍历
string = 'abc'
for x in string:
    print(x)

# from collections import Iterable  导包,判断是否可以迭代
from collections import Iterable
print(isinstance(list,Iterable))

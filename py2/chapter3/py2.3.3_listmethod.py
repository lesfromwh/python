# 列表方法
# 1.append
# 2.count 统计出现的次数
# 3.extend
# 4.index
# 5.insert
# 6.pop 移除列表中的一个元素(默认是最后一个),并且返回该元素的值.
# 7.remove
# 8.reverse 改变了列表
# 9.sort 没有返回值.
list = [1, 2, 3]
list.append(4)
print(list)  # [1, 2, 3, 4]

print(list.count(1))  # 1
print(list.count(0))  # 0

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]
# extend修改了被拓展的序列. 相比于原始的连接(+)则不然,它会返回一个全新的列表.
c = [1, 2, 3]
d = [4, 5, 6]
e = c + d  # 返回一个全新的列表e
print(e)  # [1, 2, 3, 4, 5, 6]

print(list.index(1))  # 0
# print(list.index(5))  # 报错 5 is not in list

numbers = [1, 2, 3, 4, 5]
numbers.insert(3, 99)
print(numbers)  # [1, 2, 3, 99, 4, 5]

x = [1, 2, 3, 4]
pop = x.pop()  # 4
print(pop)
print(x)  # [1, 2, 3]
x.pop(1)
print(x)  # [1, 3]

x2 = [1, 2, 3, 4, 5, 6, 7]
x2.remove(1)
# x2.remove(0) # x not in list
print(x2)

x3 = [1, 2, 3]
x3.reverse()
print(x3)  # [3, 2, 1]

x4 = [1, 2, 6, 3, 0, 12, 9]
x4.sort()
print(x4)  # [0, 1, 2, 3, 6, 9, 12]

x5 = ['addvark', 'abalone', 'acme', 'add', 'aerate']
x5.sort(key=len)
# x5.sort(key=len()) 报错
print(x5)  # ['add', 'acme', 'aerate', 'addvark', 'abalone']

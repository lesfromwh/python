print("helloworld")

# 判断
a = 100
if a > 10:
    print("> 10")
else:
    print("<10")

# 集合
arr = ["asfs", "sfas"]
print(arr[0])
print(len(arr))

# 循环
arr = [1, 2, 3, 4, 5]
for x in arr:
    print(x)

sum = 0
n = 10
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# dict Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
arr = {'l': 100, 'wb': 99, 111: 1, "ls": 99}
print(arr['l'])
print(arr[111])
# 如果 key 不存在会报错.
# 可以实现判断key是否存在.    x in arr
print(x in arr)
# 如果没有 返回none  返回None的时候Python的交互式命令行不显示结果
print(arr.get(100))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
arr.pop('l')
print(arr)

# set

set1 = set([1, 2, 3, 5, 4, 2, 1])
print(set1)
set1.add(10)
set1.remove(1)
print(set1)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)

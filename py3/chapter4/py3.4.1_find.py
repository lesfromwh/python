# 字符串方法 find
# find 可以在一个较长的字符串中查找子串.返回子串所在位子的最左端索引.如果没有找到返回-1
print('hello world'.find('world'))  # 6

s = 'hello world hello !!!'
print(s.find('hello', 1))  # 返回 12 提供起始点,从1号索引开始查找.
print(s.find('hello', 0))  # 0
print(s.find('hello'))  # 0
print(s.find('hello', 1, 5))  # -1 提供起始点和终点.
#python惯例 含头不含尾
# 运算符
# ==
# is 比较地址值(比较同一性)
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)  # True
print(x == z)  # True
print(x is z)  # False

# in
# 字符串和序列比较 : 字符串可以按照字母顺序排列进行比较
print('alpha' < 'beta')  # True

# and 类似于 java&& 已结包含了短路.
number = 11
# if number > 10 and number < 20:
if 10 < number < 20:
    print(number)

# 断言 assert
age = 10
assert 0 < age < 100
age = -1
# assert 0 < age < 100  # assert 0 < age < 100 AssertionError

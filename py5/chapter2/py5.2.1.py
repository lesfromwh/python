# 序列解包
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

x, y = y, x
print(x, y, z)  # 2 1 3

value = 1, 2, 3
print(value)  # (1, 2, 3)
x, y, z = value
print(x, y, z)  # 1 2 3

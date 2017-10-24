# 分片(切片)
# 分片操作提供2个索引的边界,含左不含右.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:1])  # [1]
print(numbers[2:5])  # [3,4,5]
print(numbers[8:])  # [9,10]
print(numbers[11:12])  # 不报错 返回[]

print(numbers[-3:-1])  # [8,9]
print(numbers[-3:0])  # []
print(numbers[-3:])  # [8,9,10]

print(numbers[:3])  # [1,2,3]

print(numbers[:])  # [1,2,3,4,5,6,7,8,9,10]

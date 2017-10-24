# 元组 :不可变序列
arr1 = 1, 2, 3
print(arr1)  # (1, 2, 3)
arr2 = (1, 2, 3)
print(arr2)  # (1, 2, 3)

# 怎么实现一个数的元组
arr3 = 33
print(arr3) # 33  这样不行
arr4 = 33,
print(arr4) # (33,) 必须加一个逗号.
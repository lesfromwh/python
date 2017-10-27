# 循环遍历字典元素
d = {'name': 'ls', 'age': '24'}
for key in d:
    print(key)

print(d.items()) # dict_items([('name', 'ls'), ('age', '24')])
for key, value in d.items():  # 不允许直接迭代字典. items 返回以 键值对的元组
    print(key, value)

for key in d:
    print(key, d[key])

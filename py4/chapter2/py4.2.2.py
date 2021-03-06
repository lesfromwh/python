# 基本字典操作
# len(d) 返回d中项的数量
# d[k] 返回value
# del d[k] 删除键为k的项.
# k in d 是否包含.
d = dict(name='wb', age='25')
print(len(d))  # 2

# 字典与列表的区别
# 1.键类型:字典的键不一定为整型.
# 2.自动添加.即使键起初在字典中并不存在,也可以为它赋值,这样字典就会创建新的项.而列表就不行.
# 3.成员资格: 表达式k in d 查找的是键,而不是值. 列表的v in l则查找的是值,而不是索引.

# [] 列表
# {} 字典

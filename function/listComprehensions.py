# 列表生产式

print(list(range(1,11)))

#方法1
list1 = []
for x in range(1,11):
    list1.append(x*x)
print(list1)
#方法2
list1 =[x*x for x in range(1,11)]
print(list1)

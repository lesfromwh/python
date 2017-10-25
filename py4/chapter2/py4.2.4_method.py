# 字典方法
# 1.clear 2.copy 3.fromkeys

# 1.clear
d = {'name': 'ls', 'age': '24'}
d.clear()
print(d)  # {}

x = {}
y = x
x['key'] = 'value'
print(x)  # {'key': 'value'}
print(y)  # {'key': 'value'}
x = {}  # x ={} 这次操作对y没有影响
print(y)  # {'key': 'value'}
print(x)  # {}

x2 = {}
y2 = x
x2['key'] = 'value'
x.clear()
print(x)  # {}
print(y)  # {}

# 2.copy(浅拷贝)
x3 = {'username': 'admin', 'machines': ['a', 'b', 'c']}
y3 = x3.copy()
y3['username'] = 'root'
print(x3)  # {'username': 'admin', 'machines': ['a', 'b', 'c']}
print(y3)  # {'username': 'root', 'machines': ['a', 'b', 'c']}
y3['machines'].remove('a')  # 这一步并没有修改掉引用,只是把里面的内容就行了修改.
print(x3)  # {'username': 'admin', 'machines': ['b', 'c']}
print(y3)  # {'username': 'admin', 'machines': ['b', 'c']}
# copy属于浅拷贝.只会引用一层. machines这个key指向的是列表的地址.
from copy import deepcopy

d = {}
d['name'] = ['a', 'b']
c = d.copy()
dc = deepcopy(d)
d['name'].append('c')
print(d)  # {'name': ['a', 'b', 'c']}
print(c)  # {'name': ['a', 'b', 'c']}
print(dc)  # {'name': ['a', 'b']}

# 3.fromkeys 使用给定的键简历新的字典,每一个键都对应一个默认的值.
print({}.fromkeys(['name', 'age']))  # {'name': None, 'age': None}
# 如果不想使用None也可以自己提供默认值
print({}.fromkeys(['name', 'age'], 'abc'))  # {'name': 'abc', 'age': 'abc'}

# 4.get 查询
d4 = {}
# print(d['abc']) 会报错,因为不存在.但是用get就不会报错,不存在返回None
print(d.get('abc'))  # None
print(d.get('abc', 'myDefault'))  # myDefault

# 5.has_key python3.0没有了
# 6.items和iteritems
# items:将字典所有的项以列表方式返回,列表中的每一项都表示为(key,value)对的形式.无序
# iteritems:在3.x 里 用 items()替换iteritems()
d6 = {'title': 'python', 'url': 'www.python.org'}
print(d6.items())  # dict_items([('title', 'python'), ('url', 'www.python.org')])
# 7.keys,iterkeys

# 8.pop 移除
d8 = {'x': '1', 'y': '2'}
d8.pop('x')
print(d8)  # {'y': '2'}

# 9.popitem 类似于list.pop默认移除最有一个元素.但是popitem弹出的是随机项,因为字典没有顺序的概念(一般删除末尾对)
d9 = {'url': '1', 'spam': '2', 'title': '3'}
popitem = d9.popitem()
print(popitem)
# 如果字典已经为空，却调用了此方法，就报出KeyError异常

# 10.setdefault  和get方法类似利用key返回value.如果key不存在,那么就会给他set一个值(这个值默认是None).如果key存在,值返回value,不做修改.
d10 = {}
setdefault = d10.setdefault('name', 'N/A')
print(setdefault)  # N/A
print(d10)  # {'name': 'N/A'}
d10.setdefault('name', 'abc')
print(d10)  # {'name': 'N/A'}

# 11.update 可以利用一个字典更新另外一个字典
d11 = {'url': '1', 'spam': '2', 'title': '3'}
x11 = {'url': 'www.baidu.com','name':'ls'}
d11.update(x11)
print(d11) # {'url': 'www.baidu.com', 'spam': '2', 'title': '3', 'name': 'ls'}

# 12.values
d12 = {'url': '1', 'spam': '3', 'title': '3'}
print(d12.values()) # dict_values(['1', '3', '3'])
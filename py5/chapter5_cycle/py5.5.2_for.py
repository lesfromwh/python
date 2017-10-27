# for循环  能用for就不要用while
word = ['a', 'c', 'b', 'e']
for x in word:
    print(x)

for x in range(1, 10):  # 1->9 含左不含右
    print(x)

z = [('name', 'ls'), ('age', '24')]
for x, y in z:
    print(x, y)

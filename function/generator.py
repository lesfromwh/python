# generator对象  用() 有别于[]
g = (x*x for x in range(10) )
print(g)
print(next(g)) #基本不用
for x in g:
    print(x)

# 字符串格式化
format = 'hello %s %s %ss'
value = ('world', 'hot', 'a')
print(format % value)  # hello world hot as

format2 = 'Pi with three decimals %.3f' # .3代表 精度保留3位小数.
from math import pi

print(format2 % pi) # Pi with three decimals 3.142

from string import Template

s = Template('$x,golrious $x!')
substitute = s.substitute(x='slurm')
print(substitute)  # slurm,golrious slurm!

s2 = Template('s ${x} hello')
print(s2.substitute(x='abc'))  # s abc hello

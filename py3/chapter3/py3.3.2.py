# 字段宽度和精度
from math import pi

print('%10f' % pi)  # 3.141593  字段宽10
print('%10.2f' % pi)  # 3.14  字段宽10 精度2
print('%.2f' % pi)  # 3.14 精度2
# 字段宽就是在控制台输出占的宽度.如下
#  3.141593
#      3.14
# 3.14

print('%.*s' % (5, 'Gu van Rossum'))  # Gu va

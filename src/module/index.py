"""
py 中的模块，引入分为完整引入，部分引入
"""
import math
import abc as ccc

from src.self_package.module_a import varA
from utils import foo, A
from effect import bar

print('查看模块所有可用的方法或类', dir(math), '\n', math.pi)
print(dir(ccc))
print(foo, A)
print(bar)
print(varA)

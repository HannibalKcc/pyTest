from decimal import Decimal

name = 'foo'

print(name)
# 输出内存地址
print(id(name))
# 输出变量类型 <class 'str'>
print(type(name))
# 模板字符串的使用方法
print(f'123{name}', '''三引号可以
换行
换行2
''')

# 常见类型 int float bool str
'''
注意 True False 是大驼峰的
不能通过 ! 取反
通过以下方式取反
'''
boolvar = bool(1 - False)
boolvar2 = not boolvar

# 整数 int
# 二进制
print(0b111)
# 八进制
print(0o732)
# 十六进制
print(0xfff)

# 浮点数 float
print(.1 + .2)
# 精度问题通过引入 Decimal 解决
print(Decimal(.1) + Decimal(.2))

# py 是动态类型语言
v1 = '123'
v1 = 456
print(v1, type(v1))

# 运算符 + 不会帮忙做隐式转换，请手动使用 str() 函数
# v2 = '123' + 456
# print(v2)

# if 语句会做隐式转换
v3 = 123
if v3:
    print('if success')

'''
多行注释，单引号才行
'''

# 整除与求余
# 负数整除，向上取整（远离0）
print(9 / 4, 9 // 4, 9 // -4)

'''
负数求余
在数学里，"负数取余"遵循的是：

> 如果 a 与 d 是整数，d 非零，那么余数 r 满足 a = q * d + r, q 为整数，且 0 <= |r| < |d|。
由此可见，我们的被除数 a = 12, 我们的商 d = 5，那么有两个余 r 满足条件，分别是一个负的余数 r1 = -2 和正的余数 r2 = 3，并且总有规律 r1 + r2 = d。

在计算机语言中，同号的整数运算，所有语言都遵循尽量让商小的原则，所以 12 mod 5 和 -12 mod -5 是一样的方式，结果差一个符号，分别是 `2` 和 `-2`。
但是在异号的整数运算中，C 和 Java 都是尽可能让商 d 更大[1] （例如 -12 mod 5 的结果对应的是商 d = -2，余 r = -2），
而 Python 则是会让商尽可能的小（例如 -12 mod 5 的结果对应的是商 d = -3，余 r = 3）。
'''
print(9 % 4, 9 % -4)

# 值的比较
obj1 = [1, 2, 3]
obj2 = [1, 2, 3]
'''
对于引用类型， == 比较会进行值比较
而 is 是进行内存地址比较，
'''
print(1 == 2, obj1 == obj2, obj1 is obj2)

'''
布尔运算符，不合法的——
1 || 2
1 && 2
'''
print(1 and 2, 1 or 2)

print('k' in 'helloworld', 'abc' in ['123', 'abc', 34345])

# input 获取用户输入
res = input('提出问题，输入会给到函数返回值：\n')
print(f'你刚才输入的是{res}')

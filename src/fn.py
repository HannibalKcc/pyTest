# 函数
def foo(a, b):
    return a * a + b


print(foo(3, 4))
# 可以通过特殊的姿势指定实参与形参的关系
print(foo(b=3, a=4))


# 如果没有显式声明 return，则与 return None 等价
def no_return():
    print('123')


print(no_return())

# 函数可以通过 , 连接多个值并 return 出去————实际上是返回了一个元组
def return_multi(a, b, c):
    return c, b, a


print(return_multi(3, 2, 1))

# 由于 py 没有使用大括号，所以写一个条件语句的对应执行为空就变得不那么明确，为此特地有了 pass 语句的存在
x = 123
if x == 5:
    print('123')
    pass
else:
    pass


def foo():
    pass


class A:
    pass

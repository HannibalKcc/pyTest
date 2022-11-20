"""
需要注意的是，一个模块一旦被引入，会执行模块里的所有语句，比如 print
如果想要避免这种情况，可以使用变量 __name__ 做判断，如果当前模块不是被引用执行而是作为主入口执行的，那么 __name__ == '__main__'，否则会输出文件名（不含后缀）
"""

print('here is effect.py', __name__)
if __name__ == '__main__':
    print('print oly main')


def bar():
    print('effect bar')

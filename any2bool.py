"""
将任意值丢入 bool 函数进行转化的结果
注意空数组、空对象的隐式转换结果是不同于 js 的
"""
for item in ['', '1', 0, -0.0, None, [], [1], {}, (), set()]:
    print(f'{str(item)}——{bool(item)}')

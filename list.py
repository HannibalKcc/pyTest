arr = [1, 2, 3, 'str', 'str2']
print(
    id(arr), '\n',
    id(arr[0]), id(arr[1]), id(arr[2]), '\n',
    arr[-1],
)

arr.index(1)  # 返回第一个匹配的下标
# arr.index('not in') # error

# IndexError: list index out of range
# print([4, 5, 6][100])

# 获取多个元素，使用切片
print(arr[1: 5], arr[2:4:1])
print(arr[:: -1], arr[-2:: -1])


arr = [10, 20, 30, 40]
arr.remove(30)
print(arr)

# 删除指定索引上的元素
arr.pop(1)
print(arr)
# 删除最后一个元素
arr.pop()
print(arr)

# 切片也可以用于删除元素，注意有影响原元素与不影响两种写法
arr2 = [7, 8, 9, 0, 1, 2, 3, 4]
print(arr2[1:3], arr2)

arr2[1: 3] = []
print(arr2)

arr2 = [1, 2, 3]
arr3 = [7, 8, 9]
print(id(arr2), id(arr3))

# 增加元素
arr2.append(44)
print(arr2)
arr2.extend([4, 5, 6])
print(arr2)
arr2.insert(0, 'hello')
print(arr2)

# 切片也可以用来增加元素
arr2[1:2] = ['a', 'b', 'c']
print(arr2)
arr2[1:] = ['x', 'y', 'z']
print(arr2)

arr = [432, 23, 22, 1, 4, 93, 234, 22]
# 变异函数，默认升序
arr.sort()
print(arr)
# 降序
arr.sort(reverse=True)
print(arr)
# 不可变异
print(sorted(arr))

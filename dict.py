# 字典 两种创建方式
dict1 = dict(name='jack', age=20)
# key 必须使用引号
dict2 = {
    'a': 123,
    "b": 456,
}

print(dict1, dict2)

'''
字典值的获取方式也有两种
如果对应的 key 不存在于字典中，使用 [] 取会异常，get() 则拿到一个 None
'''
print(dict1['name'], dict2.get('a'))

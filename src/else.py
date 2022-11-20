'''
else 语句可以余 while 或者 for 搭配使用
'''
for num in range(2):
    res = input('输入数字，0 或其他值')
    if res == '0':
        print('输入 0 结束了')
        break
    print(f'here is {res}')
else:
    print('从未输入 0')

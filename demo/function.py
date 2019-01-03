# def ifun(name,age=23,addr='shanghai'):
#     print(age,name,addr)

# ifun(age=1,addr='bj',name='bob')


L1 = [1,2,3,4,5]

# def func(x):
#     return x>3

# list = filter(func,L1)

# res = [item for item in list]

# print(res)

print([item for item in filter(lambda x:x>3,L1)])
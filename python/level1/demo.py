# 假定有a班和b班
# a班有同学：aa, ab, ac, ad, ae
a = ['aa', 'ab', 'ac', 'ad', 'ae']
# b班有同学：ba，bb, bc, bd, be
b = ['ba', 'bb', 'bc', 'bd', 'be']
# 1、现在要将两个班级合并，求新班级的人员列表
x = []
# x.extend('aa', 'ab', 'ac', 'ad', 'ae', 'ba', 'bb', 'bc', 'bd', 'be')
x.extend(a)
x.extend(b)
print('新班级的人员列表是')
print(x)
# 2、其中叫aa, bb的同学转学，求新班级的人员列表
print('aa, bb转学后，新班级的人员列表是')
x.remove('aa')
x.remove('bb')
print(x)
# 3、其中叫ab的同学，改名叫abb
x[0] = 'abb'
print(x)
x.pop(0)
x.insert(0, 'abb')
print(x)
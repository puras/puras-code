'''
s = 0

for i in range(101):
    s = s + i

print(s)
'''

'''
s = 1
for i in range(10):
    s *= (i + 1)
print(s)
'''

# 将从1到100中的所有奇数相加，输出它们的和
# s = 0
# for i in range(101):
#     if i % 2 != 0:
#         s = s + i
# print(s)

# for i in range(0, 10, 2):
#     print(i)

# s = 1
# for i in range(1, 10, 2):
#     s = s * i
# print(s)

# x = 1
# y = 1
# print(x)
# print(y)
# for i in range(10):
#     s = x + y
#     x = y
#     y = s
#     print(s)


x = [1, 1]
for i in range(20):
    x.append(x[i] + x[i + 1])
print(x)
# for i in range(101):
#     print(i)

# x = 1
# y = 1
# ret = [x, y]
# for i in range(10):
#     s = x + y
#     x = y
#     y = s
#     ret.append(s)
#
# print(ret)
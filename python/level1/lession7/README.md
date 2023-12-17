列表
----

# 知识点

## 列表的定义和创建

列表List是Python中常见的一种数据类型。用一对中括号来表示，中间用逗号隔开。

例如：
```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
```

列表里的内容，称之为元素。

列表元素可以由多种数据类型组成，同样也可以包含列表。

## 索引和切片

### 索引

为列表中元素的编号(支持负数索引)

例如：
```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
# 索引       0         1       2      3       4
# 负数索引   -5        -4      -3     -2      -1
print(students[0])
```

注意：Python中索引是从0开始，第一个元素的索引为0，而不是1.

### 切片

从列表中选取子列表的操作，基本形式是sequence[start:stop:step]，其中start表示起始位置(包含)，stop表示结束位置(不包含)，step表示步长

例如：

```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
print(students[2:4])
```

输出：
 
```
['Jim', 'Mike']
```

省略冒号前面的数字，表示从列表的第一个元素开始；省略冒号后面的数据表示到列表的结尾；只写冒号，就返回原有列表所有元素。

## 列表的增删改

### 添加元素

第一种：append   
一次只能向列表中添加一个元素

```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
students.append('Lily')
```

第二种：extend   
一次可以向列表中添加多个元素

```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
students.extends(['Lily', 'Twist'])
```

第三种：insert   
在原列表指定位置插入元素

```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
students.insert(1, 'Lily')
```

### 删除元素

第一种：pop
通过元素的索引来删除元素

```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
students.pop(1)
```

第二种：remove    
通过元素的值来删除元素

```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
students.remove('Bob')
```

注意：如果列表中有多个重复的值，该方法仅删除第一个，如想将全部重复的值都删除掉，可以多次调用该方法

### 修改元素

通过列表索引获取指定元素，对其进行重新赋值以达到修改元素的效果

```
students = ['Bob', 'Alice', 'Jim', 'Mike', 'Judy']
students[0] = 'Jack'
```

# 示例程序

```
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
```

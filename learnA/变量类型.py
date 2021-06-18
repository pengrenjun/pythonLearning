# coding=utf-8
"""
变量存储在内存中的值，这就意味着在创建变量时会在内存中开辟一个空间。
基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符

每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号 = 用来给变量赋值

"""

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name

# Python允许你同时为多个变量赋值
a = b = c = 1
print a,b,c
a, b, c = 1, 2, "john"
print a,b,c

"""
Python有五个标准的数据类型：

Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

"""

"""
Python支持四种不同的数字类型
int（有符号整型） 100  -786  -0490  -0x260  0x69
long（长整型[也可以代表八进制和十六进制]） 	51924361L  -0x19323L 0122L  0xDEFABCECBDAECBFBAEl
float（浮点型） 0.0  -21.9  32.3e+18   -32.54e100   70.2E-12
complex（复数） 3.14j  9.322e-36j  -.6545+0J 	3e+26J

Python 支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

注意：long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。
"""

"""
Python字符串
字符串或串(String)是由数字、字母、下划线组成的一串字符

python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
如果你要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符

加号（+）是字符串连接运算符，星号（*）是重复操作。
"""

s = 'abcdef'
print s[1:5]
print s[5]
print s[-3:-1]

str = 'Hello World!'

print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第六个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

"""
Python列表

List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

加号 + 是列表连接运算符，星号 * 是重复操作
"""
print ('==============List=======================')
list1 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
combList = [123, 'john',[123,123456]]

print list1 , combList    # 输出完整列表
print list1[0]
print combList[2][1]  # 输出列表的第一个元素
print list1[1:3]          # 输出第二个至第三个元素
print list1[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list1 + tinylist    # 打印组合的列表
tinylist.append(123)
print tinylist

"""
Python 元组
元组是另一个数据类型，类似于 List（列表）。
元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

"""
print ('==============tuple=======================')
tuple1 = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple1               # 输出完整元组
print tuple1[0]            # 输出元组的第一个元素
print tuple1[1:3]          # 输出第二个至第四个（不包含）的元素
print tuple1[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple1 + tinytuple   # 打印组合的元组

print ('==============test modify tuple=======================')
tuple1 = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list2 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list2[2] = 1000     # 列表中是合法应用
print tuple1
print list2

"""
Python 字典
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。
列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
"""
print ('==============dictionary=======================')
dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"

tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}


print dict1['one']          # 输出键为'one' 的值
print dict1[2]              # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值
print tinydict['name']


"""
数据类型转换函数
int(x [,base])          将x转换为一个整数

long(x [,base] )        将x转换为一个长整数

float(x)                将x转换到一个浮点数

complex(real [,imag])   创建一个复数 complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
如果第一个参数为字符串，则不需要指定第二个参数。

str(x)                  将对象 x 转换为字符串

repr(x)                 将对象 x 转换为表达式字符串

eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象 eval(expression[, globals[, locals]])

tuple(s)                将序列 s 转换为一个元组

list(s)                 将序列 s 转换为一个列表

set(s)                  转换为可变集合  set(s) 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

dict(d)                 创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)            转换为不可变集合

chr(i)                  将一个整数转换为一个字符 chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
i -- 可以是10进制也可以是16进制的形式的数字。  返回值是当前整数对应的 ASCII 字符。

unichr(x)               将一个整数转换为Unicode字符

ord(x)                  将一个字符转换为它的整数值

hex(x)                  将一个整数转换为一个十六进制字符串

oct(x)                  将一个整数转换为一个八进制字符串
"""

print ('==============int(x [,base]) =======================')
print int()               # 不传入参数时，得到结果0

print int(3)

print int(3.6)

print int('12',16)        # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制

print int('0xa',16)

print int('10',8)

print int('0x19',16)

print int('0111',2)

print ('==============float(x)  =======================')
print float('100')

print ('==============complex(real [,imag])  =======================')
print complex(1, 2)

print complex(1)    # 数字

print complex("1")  # 当做字符串处理

# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print complex("1+2j")

print ('==============evel(expression) =======================')
x = 7
print eval( '3 * x' )

print eval('pow(2,2)')

print eval('2 + 2')

print ('==============tuple(s) =======================')
print tuple([1,2,3,4])

print tuple({1:2,3:4})    #针对字典 会返回字典的key组成的tuple
 
print tuple((1,2,3,4))    #元组会返回元组自身

aList = [123, 'xyz', 'zara', 'abc'];
aTuple = tuple(aList)

print "Tuple elements : ", aTuple

test_list1 = ('a','b','c')
test_list2 = ['x','y','z']
test_tuple = tuple(test_list2)
# test_list2 可以修改，tuple() 函数不是改变值的类型，而是返回改变类型后的值，原值不会被改变
test_list2[2] = 'adf'
#下面这行报错，元组不可修改
# test_list1[2]='这是修改的'
print(test_list1)
print(test_list2)
print(test_tuple)

print ('==============list(tup) =======================')
aTuple = (123, 'runoob', 'google', 'abc');
aList = list(aTuple)

print ("列表元素 : ")
print(aList)

print ('==============set(s) =======================')
x = set('runoob')
y = set('google')
print x,y
# (set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
print x & y         # 交集
# set(['o'])
print x | y         # 并集
# set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
print x - y         # 差集
# set(['r', 'b', 'u', 'n'])
print x^y           #补集  返回一个新的集合，包括集合 x 和 y 的非共同元素

print list(x - y)
print tuple(x - y)


print ('==============dict(s) =======================')

print dict()                        # 创建空字典

print dict(a='a', b='b', t='t')     # 传入关键字

print dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典

print dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典

print ('==============char(i) =======================')
print chr(0x30), chr(0x31), chr(0x61)   # 十六进制 -> ASCII
print chr(48), chr(49), chr(97)         # 十进制 -> ASCII

print ('==============ord(c) =======================')
print ord('0') # 返回值是对应的十进制整数
print ord('1')
print ord('a')

print ('==============hex(i) =======================')
print hex(21) # 十进制->十六进制
print hex(100)
print hex(-42)

print ('==============oct(i) =======================')
print oct(21) # 十进制->8进制
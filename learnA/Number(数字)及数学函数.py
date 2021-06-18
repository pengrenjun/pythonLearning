# coding=utf-8

"""
Python Number 类型转换函数
int(x [,base ])         将x转换为一个整数
long(x [,base ])        将x转换为一个长整数
float(x )               将x转换到一个浮点数
complex(real [,imag ])  创建一个复数
str(x )                 将对象 x 转换为字符串
repr(x )                将对象 x 转换为表达式字符串
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )               将序列 s 转换为一个元组
list(s )                将序列 s 转换为一个列表
chr(x )                 将一个整数转换为一个字符
unichr(x )              将一个整数转换为Unicode字符
ord(x )                 将一个字符转换为它的整数值
hex(x )                 将一个整数转换为一个十六进制字符串
oct(x )                 将一个整数转换为一个八进制字符串
"""


"""
Python math 模块、cmath 模块
Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。

Python math 模块提供了许多对浮点数的数学运算函数。

Python cmath 模块包含了一些用于复数运算的函数。

cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。

要使用 math 或 cmath 函数必须先导入：
import math

"""
import math,cmath
print dir(math)
print dir(cmath)

"""
Python数学函数
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根
"""
print "cmp(80, 100) : ", cmp(80, 100)
print "cmp(180, 100) : ", cmp(180, 100)
print "cmp(-80, 100) : ", cmp(-80, 100)
print "cmp(80, -100) : ", cmp(80, -100)

print "math.fabs(-45.17) : ", math.fabs(-45.17)
print "math.fabs(100.12) : ", math.fabs(100.12)
print "math.fabs(100.72) : ", math.fabs(100.72)
print "math.fabs(119L) : ", math.fabs(119L)
print "math.fabs(math.pi) : ", math.fabs(math.pi)

print "max(80, 100, 1000) : ", max(80, 100, 1000)
print "max('1,2,3,4') : ", max('1,2,3,4')
print "max([1,2,3,4]) : ", max([1,2,3,4])

print "max([(1,2),(2,3),(3,4)]) : ", max([(1,2),(2,3),(3,4)])  # 按照元素里面元组的第一个元素的排列顺序，输出最大值（如果第一个元素相同，则比较第二个元素，输出最大值） 据推理是按ascii码进行排序的
print "max({1:2,2:2,3:1,4:'aa'})  : ", max({1:2,2:2,3:1,4:'aa'}) # 比较字典里面的最大值，会输出最大的键值


print "math.modf(100.12) : ", math.modf(100.12)
print "math.modf(100.72) : ", math.modf(100.72)
print "math.modf(119L) : ", math.modf(119L)
print "math.modf(math.pi) : ", math.modf(math.pi)

# 第一个参数是一个浮点数，第二个参数是保留的小数位数，可选，如果不写的话默认保留到整数
'''
https://www.runoob.com/w3cnote/python-round-func-note.html
round() 保留小数会有小问题
除非对精确度没什么要求，否则尽量避开用round()函数。近似计算我们还有其他的选择：
使用math模块中的一些函数，比如math.ceiling（天花板除法）。
python自带整除，python2中是/，3中是//，还有div函数。
字符串格式化可以做截断使用，例如 "%.2f" % value（保留两位小数并变成字符串……如果还想用浮点数请披上float()的外衣）。
当然，对浮点数精度要求如果很高的话，请用嘚瑟馍，不对不对，请用decimal模块。
'''
print "round(80.23456, 2) : ", round(80.23456, 2)
print "round(80.23556, 2) : ", round(80.23556, 2)
print "round(2.355, 2) : ", round(2.355, 2) # round函数并不总是如上所说的四舍五入
print "round(100.000056, 3) : ", round(100.000056, 3)
print "round(20/7) : ", round(20/7) # 不写默认保留到整数

"""
Python随机数函数
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	随机生成下一个实数，它在[0,1)范围内。
randint(x,y) 随机生成一个整数，它在[x,y]范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
"""
import random
print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A String') : ", random.choice('A String')

# randrange 入参为整数
# 输出 100 <= number < 1000 间的偶数
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

# 输出 100 <= number < 1000 间的其他数
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)


# 生成第一个随机数
print "random() : ", random.random()

# 生成第二个随机数
print "random() : ", random.random()
print "random.randint(1,10) : ", random.randint(1,10)  # 产生 1 到 10 的一个整数型随机数

'''
我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。
但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，
这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。
'''
print "------- 设置种子 seed 前 -------"
print random.random()
print random.random()

print "------- 设置种子 seed 后-------"
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

random.seed( 10 )
print "Random number with seed 10 : ", random.random()

random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# 生成同一个随机数
random.seed( 9 )
print "Random number with seed 9 : ", random.random()

# 生成同一个随机数
random.seed( 9 )
print "Random number with seed 9 : ", random.random()

random.seed( 9 )
print "Random number with seed 9 : ", random.random()

list1 = [20, 16, 10, 5]
random.shuffle(list1)
print "随机排序列表 : ",  list1

random.shuffle(list1)
print "随机排序列表 : ",  list1

'''
uniform() 方法将随机生成下一个实数，它在 [x, y] 范围内
返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x
'''
print "uniform(5, 10) 的随机数为 : ",  random.uniform(5, 10)

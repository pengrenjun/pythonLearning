# coding=utf-8

'''
Python 访问字符串中的值

Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python 访问子字符串，可以使用方括号来截取字符串
'''

var1 = 'Hello World!'
var2 = "Python Runoob"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]


# Python 字符串连接
var1 = 'Hello World!'
print "输出 :- ", var1[:6] + 'Runoob!'


'''
Python字符串运算符
'''
print ('====Python字符串运算符======')
a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if( "H" in a) :
    print "H 在变量 a 中"
else :
    print "H 不在变量 a 中"

if( "M" not in a) :
    print "M 不在变量 a 中"
else :
    print "M 在变量 a 中"

# 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
# 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
print r'\n'
print R'\n'

'''
Python 字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %F 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
'''
print "My name is %s and weight is %d kg!" % ('Zara', 21)

'''
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

基本语法是通过 {} 和 : 来代替以前的 % 。
format 函数可以接受不限个参数，位置可以不按顺序

>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
'''
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print '=====str.format()==================='
# str.format() 数字格式化
'''
3.1415926	{:.2f}	3.14	保留小数点后两位
3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
-1	{:+.2f}	-1.00	带符号保留小数点后两位
2.71828	{:.0f}	3	不带小数
5	{:0>2d}	05	数字补零 (填充左边, 宽度为2)
5	{:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
10	{:x<4d}	10xx	数字补x (填充右边, 宽度为4)
1000000	{:,}	1,000,000	以逗号分隔的数字格式
0.25	{:.2%}	25.00%	百分比格式
1000000000	{:.2e}	1.00e+09	指数记法
13	{:>10d}	        13	右对齐 (默认, 宽度为10)
13	{:<10d}	13	左对齐 (宽度为10)
13	{:^10d}	    13	中间对齐 (宽度为10)
11	
'{:b}'.format(11)
'{:d}'.format(11)
'{:o}'.format(11)
'{:x}'.format(11)
'{:#x}'.format(11)
'{:#X}'.format(11)	
1011
11
13
b
0xb
0XB	进制

^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。

此外我们可以使用大括号 {} 来转义大括号，如下实例：  print ("{} 对应的位置是 {{0}}".format("runoob"))
'''
print("{0:.2f}".format(3.1415926))
print("{:.2f}".format(3.1415926))
print ("{} 对应的位置是 {{0}}".format("runoob"))

#在字段后的 : 后面加一个整数会限定该字段的最小宽度，这在美化表格时很有用
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10,.2f}'.format(name, phone))

#可以用 ** 标志将这个字典以关键字参数的方式传入
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 元组的 format 用法
k=("name","mh")
v="名字：{0},name:{1}".format(*k)
print(v)


print '===python的字符串内建函数====='
'''
python的字符串内建函数
字符串方法是从python1.6到2.0慢慢加进来的——它们也被加到了Jython中。
这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的

string.capitalize()                                 capitalize() 将字符串的第一个字母变成大写,其他字母变小写

string.center(width)                                返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
                                                    str.center(20, '*')  str.center(20)

string.count(str, beg=0, end=len(string))           返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

string.decode(encoding='UTF-8', errors='strict')    以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'

string.encode(encoding='UTF-8', errors='strict')    以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

string.endswith(obj, beg=0, end=len(string))        检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

string.expandtabs(tabsize=8)                        把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。

string.find(str, beg=0, end=len(string))            检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1

string.format()                                     格式化字符串

string.index(str, beg=0, end=len(string))           跟find()方法一样，只不过如果str不在 string中会报一个异常.

string.isalnum()                                    如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

string.isalpha()                                    如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

string.isdecimal()                                  如果 string 只包含十进制数字则返回 True 否则返回 False.

string.isdigit()                                    如果 string 只包含数字则返回 True 否则返回 False.

string.islower()                                    如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

string.isnumeric()                                  如果 string 中只包含数字字符，则返回 True，否则返回 False

string.isspace()                                    如果 string 中只包含空格，则返回 True，否则返回 False.

string.istitle()                                    如果 string 是标题化的(见 title())则返回 True，否则返回 False

string.isupper()                                    如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

string.join(seq)                                    以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

string.ljust(width)                                 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

string.lower()                                      转换 string 中所有大写字符为小写.

string.lstrip()                                     截掉 string 左边的空格

string.maketrans(intab, outtab)                     maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)                                            返回字符串 str 中最大的字母。

min(str)                                            返回字符串 str 中最小的字母。

string.partition(str)

有点像 find()和 split()的结合体,从 str 出现的第一个位置起,
把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.

string.replace(str1, str2,  num=string.count(str1)) 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

string.rfind(str, beg=0,end=len(string) )           类似于 find() 函数，返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。

string.rindex( str, beg=0,end=len(string))          类似于 index()，不过是从右边开始.

string.rjust(width)                                 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

string.rpartition(str)                              类似于 partition()函数,不过是从右边开始查找

string.rstrip()                                     删除 string 字符串末尾的空格.

string.split(str="", num=string.count(str))         以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+1 个子字符串

string.splitlines([keepends])                       按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

string.startswith(obj, beg=0,end=len(string))       检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

string.strip([obj])                                 在 string 上执行 lstrip()和 rstrip()

string.swapcase()                                   翻转 string 中的大小写

string.title()                                      返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

string.translate(str, del="")                       根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中

string.upper()                                      转换 string 中的小写字母为大写

string.zfill(width)                                 返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
'''

str = "this is string example....wow!!!";
sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

str = "this is string example....wow!!!";
str = str.encode('base64','strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')

str1 = "this is string example....wow!!!";
str2 = "exam";
# 如果包含子字符串返回开始的索引值，否则返回-1
print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

print str1.index(str2);
print str1.index(str2, 10);
#  print str1.index(str2, 40); 该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常

str = "this2009";  # 字符中没有空格 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print str.isalnum();

str = "this is string example....wow!!!";
print str.isalnum();

# 如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False
str = "runoob";
print str.isalpha();

str = "runoob菜鸟教程";
print str.isalpha();

str = "this is string example....wow!!!";
print str.isalpha();

# Python isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
# 注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。

str = u"this2009";
print str.isdecimal();

str = u"23443434";
print str.isdecimal();

# Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
#注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可
# 对于 Unicode 数字、全角数字（双字节）、罗马数字和汉字数字会返回 True ，其他会返回 False  ； byte数字（单字节）无此方法
str = u"this2009";
print str.isnumeric();

str = u"23443434";
print str.isnumeric();

'''
isdigit()

True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字

False: 汉字数字

Error: 无

isdecimal()

True: Unicode数字，，全角数字（双字节）

False: 罗马数字，汉字数字

Error: byte数字（单字节）

isnumeric()

True: Unicode数字，全角数字（双字节），罗马数字，汉字数字

False: 无

Error: byte数字（单字节）
'''

num = u"1"  #unicode
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = "1" # 全角
num.isdigit()   # True
# num.isdecimal() # True
# num.isnumeric() # True

num = b"1" # byte
num.isdigit()   # True
#num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
#num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'

num = "IV" # 罗马数字
num.isdigit()   # True
# num.isdecimal() # False py3
# num.isnumeric() # True  py3

num ="四" # 汉字
num.isdigit()   # False
#num.isdecimal() # False  py3
#num.isnumeric() # True  py3

# Python istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
str = "This Is String Example...Wow!!!";
print str.istitle();


'''
join 列表中的元素也需要是字符串

>>> print(''.join([1,2,3,4]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found
此时会报错，而当列表元素为字符串时，正常运行：

>>> print(','.join(['1','2','3','4']))
1,2,3,4

'''
str = "This is string example....wow!!!";
print str.istitle();

list=['1','2','3','4','5']
print(''.join(list))
seq = {'hello':'nihao','good':2,'boy':3,'doiido':4}
print('-'.join(seq))

str = "this is string example....wow!!!";

print str.ljust(50, '0');

'''
Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

注：两个字符串的长度必须相同，为一一对应的关系。

'''

from string import maketrans   # 必须调用 maketrans 函数。

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab);

# 关于 string 的 replace 方法，需要注意 replace 不会改变原 string 的内容
str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3)

#Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );       # 以空格为分隔符，包含 \n
print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个

txt = "Google#Runoob#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)
print x

'''
Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
'''
str1 = 'ab c\n\nde fg\rkl\r\n'
print str1.splitlines();

str2 = 'ab c\n\nde fg\rkl\r\n'
print str2.splitlines(True)


'''
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

'''
str = "00000003210Runoob01230000000";
print str.strip( '0' );  # 去除首尾字符 0


str2 = "   Runoob      ";   # 去除首尾空格
print str2.strip();

#Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。

from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab, 'xm');






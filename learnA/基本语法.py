# coding=utf-8

# 说明：Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断
# python 最具特色的就是用缩进来写模块。缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。 因此，在 Python 的代码块中必须使用相同数目的行首缩进空格数。
"""
 缩进相同的一组语句构成一个代码块，我们称之代码组。

 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)
"""
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错 IndentationError: unindent does not match any outer indentation level
    print ("False")

# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须是相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# python 中多行注释使用三个单引号(''')或三个双引号(""")。 python中单行注释采用 # 开头
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 下面的程序执行后就会等待用户输入，按回车键后就会退出：
raw_input("按下 enter 键退出，其他任意键显示...\n")

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
import main; main.print_hi('中国')


x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
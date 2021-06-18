# coding=utf-8

"""
由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现
如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；
使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
"""

num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello

num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine


"""
Python 没有 switch/case 语句，如果遇到很多中情况的时候，写很多的 if/else 不是很好维护，这时可以考虑用字典映射的方法替代：

"""
import os
def zero():
    return "zero"

def one():
    return "one"

def two():
    return "two"

def num2Str(arg):
    switcher={
        0:zero,
        1:one,
        2:two,
        3:lambda:"three"
    }
    func=switcher.get(arg,lambda:"nothing")
    return func()

if __name__ == '__main__':
    print num2Str(1)
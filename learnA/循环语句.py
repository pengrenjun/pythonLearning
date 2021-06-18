# coding=utf-8

"""
Python 提供了 for 循环和 while 循环（在 Python 中没有 do..while 循环）
循环类型	描述
while 循环	在给定的判断条件为 true 时执行循环体，否则退出循环体。
for 循环	重复执行语句
嵌套循环	你可以在while循环体中嵌套for循环

循环控制语句
break 语句	在语句块执行过程中终止循环，并且跳出整个循环
continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass 语句	pass是空语句，是为了保持程序结构的完整性。
"""

def deduplication(self, nums):#找出排序数组的索引
    for i in range(len(nums)):
        if nums[i]==self:
            return i
    i=0
    for x in nums:
        if self>x:
            i+=1
    return i

print(deduplication(0, [1,3,5,6]))


def deduplication2(self, nums):
    if self in nums:                  #加入数字是否在数组的判断，不在则打印none
        for i in range(len(nums)):    #一个for循环加上if else即可找出数组索引
            if nums[i] == self:
                return i
            else:
                i += 1
        return i

print(deduplication2(5, [1, 3, 5, 6]))

# continue 和 break 用法

print("======continue break========")
i = 1
while i < 10:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

# 循环使用 else 语句  在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
print ("==while … else ==")
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

#九九乘法表

print("====九九乘法表=========")
i = 1
while i :
    j = 1
    while j:
        print j ,"*", i ," = " , i * j , '  ',
        if i == j :
            break

        j += 1
        if j >= 10:
            break

    print "\n"
    i += 1
    if i >= 10:
        break


print ("===Pyhton 去除字符串首尾的空格：=====")
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

str = '   Runoob     '
print(trim(str))


"""
Python for 循环语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

语法：
for循环的语法格式如下：

for iterating_var in sequence:
   statements(s)   
"""
print ("====for====")
str='asdfadsf'
for var in str:
    print var,

print ''

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit

tuples = (1, 2,  3)
for num in tuples:        # 第二个实例
   print '当前num :', num


# 通过序列索引迭代
print '======通过序列索引迭代========'
fruits = ['banana', 'apple',  'mango']
print 'range():',range(len(fruits))
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]
# 以上实例我们使用了内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数

# 使用内置 enumerate 函数进行遍历
print '======使用内置 enumerate 函数进行遍历======'
for (i, j) in enumerate(fruits):
    print i,j

'''在python中，for循环后的in跟随一个序列的话，循环每次使用的序列元素，而不是序列
的下标'''
print ("=====for range,enumerate====== ")
s = 'qazxswedcvfr'
for i in range(0,len(s),2):
    print s[i]
'''enumerate() :
    在每次循环中，可以同时得到下标和元素
    际上，enumerate(),在每次循环中返回的是包含每个元素的定值表，两个元素分别赋值
 index，char'''
for (index,char) in enumerate(s):
    print "index=%s ,char=%s" % (index,char)

#for...else 在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
# while … else 也是一样
print '====for..else========'
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

print '===Python 循环嵌套====='
#使用了嵌套循环输出2~100之间的素数
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1


#冒泡排序
print '====冒泡排序========'
array = [9,2,7,4,5,6,3,8,1,10]
L = len(array)
for i in range(L):
    for j in range(L-i):
        if array[L-j-1]<array[L-j-2]:
            array[L-j-1],array[L-j-2]=array[L-j-2],array[L-j-1]
for i in range(L):
    print array[i],

print ' '
#Python pass 语句 Python pass 是空语句，是为了保持程序结构的完整性。 pass 不做任何事情，一般用做占位语句。
print('===pass=======')
# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter


'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-08 11:34:54
LastEditors: Liang Anqing
LastEditTime: 2020-09-08 11:53:27
'''
'''
[编程题]复数乘法

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M
输入两个表示复数的字符串，输出它们相乘的结果的字符串
复数字符串用a+bi表示(a, b 为整数, i为虚数单位，i2=1)

输入描述:

两个表示复数的字符串


输出描述:

两个数相乘的结果的字符串


输入例子1:

1+2i
2+1


输出例子1:

0+5i


例子说明1:

(1+2i)(2+i) = (2 + i + 4i + 2i * i) = 0 + 5i


输入例子2:

1+-2i
3+4i


输出例子2:

11+-2i


例子说明2:


(1+-2i)(3+4i) = (3 + 4i - 6i - 8i * i) = 11+-2i

'''
def solution(a,b):
    temp=list(map(lambda x:x.replace('i',''),[a,b]))
    x=list(map(int,temp[0].split('+')))
    y=list(map(int,temp[1].split('+')))
    n=x[0]*y[0]-x[1]*y[1]
    m=x[0]*y[1]+x[1]*y[0]
    res=str(n)+'+'+str(m)+'i'
    print(res)
if __name__=='__main__':
    a=input()
    b=input()
    solution(a,b)
'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-08 12:59:10
LastEditors: Liang Anqing
LastEditTime: 2020-09-08 13:07:45
'''
'''
一年中的第几天

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M
输入一个"YYYY-MM-dd"格式的日期字符串，输出该天是当年的第几天（1 月 1 日是每年的第 1 天）

输入描述:

一个"YYYY-MM-dd"格式的表示日期的字符串


输出描述:

该天是当年的第几天


输入例子1:

2019-01-09


输出例子1:

9


输入例子2:

2004-03-01


输出例子2:

61


例子说明2:

2004年为闰年，所以是第31+29+1=61天

'''
def solution(s):
    year,month,day=list(map(int,s.split('-')))
    if (year%4==0 and year%100>0) or year%400==0:
        is_LearYear=True
    else:
        is_LearYear=False
    for i in range(month):
        if i==0:
            continue
        if (i<8 and i%2==1) or (i>=8 and i%2==0):
            day+=31
        elif i==2:
            day+=29 if is_LearYear else 28
        else:
            day+=30
    print(day)
if __name__=='__main__':
    s=input()
    solution(s)
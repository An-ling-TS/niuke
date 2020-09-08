'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-08 14:54:33
LastEditors: Liang Anqing
LastEditTime: 2020-09-08 15:11:49
'''
'''
Check if the given string is a valid string literal.

输入描述:

A double quoted string


输出描述:

true or false


输入例子1:

"abc"


输出例子1:

true


输入例子2:

"abc


输出例子2:

false

'''
def solution(s):
    s=s.replace('\\\\','')

    size=len(s)
    if size<2:
        print('false')
        return

    if s[0]!='\"' or s[size-1]!='\"' or s[size-2]=='\\':
        print('false')
        return
    for i in range(size):
        if i==size-1 or i==0:
            continue
        if s[i]=='\"' and s[i-1]!='\\':
            print('false')
            return
    print('true')
if __name__=='__main__':
    s=input()
    solution(s)
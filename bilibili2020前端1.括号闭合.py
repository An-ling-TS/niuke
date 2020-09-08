'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-17 16:19:11
LastEditors: Liang Anqing
LastEditTime: 2020-08-17 16:33:38
'''
'''

判断由"()[]{}"6种括号组成的字符串是否合法
1. 所有括号必须闭合
2. 左括号必须在正确的位置闭合

输入描述:

由6种符号组成的字符串


输出描述:

合法则输出"true"，不合法输出"false"


输入例子1:

(]


输出例子1:

false


输入例子2:

{[][()()]}


输出例子2:

true


输入例子3:

{([)]}


输出例子3:

false

'''
def solution(s):
    stack=[]
    if s=='':
        return 'true'
    
    size=len(s)
    for i in s:
        if i=='(' or i=='[' or i=='{':
            stack.append(i)
            continue
        temp=''
        if i==')':
            flag='('
        if i=='}':
            flag='{'
        if i==']':
            flag='['
        if stack.pop()!=flag:
            return 'false'
        return 'true'
    
    if len(stack)==0:
        return 'true'
    return 'false'
        
if __name__=='__main__':
    s=input()
    print(solution(s))
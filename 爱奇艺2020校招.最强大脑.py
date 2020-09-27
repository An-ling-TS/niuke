'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-10 18:39:03
LastEditors: Liang Anqing
LastEditTime: 2020-09-10 18:56:45
'''
'''
 人脑对于长度特别长的字符串的处理速度是有限的，但是最强大脑挑战的就是人脑的极限，现在有这样一项挑战，给出一个很长的字符串S，和一个较短的字符串T，请你求出对于每一个前缀[1,r]内有多少个T字符串。

输入描述:

第一行一个字符串S。

第二行一个字符串T。两个字符串保证均只含小写字母。（1≤|S|≤500000, 1≤|T|≤100）


输出描述:

输出仅包含|S|个正整数，分别表示[1,r]内有多少个T字符串。(1<=r<=|S|)


输入例子1:

ababac
ab


输出例子1:

0 1 1 2 2 2

'''
def solution(s,t):
    t_size=len(t)
    s_size=len(s)
    rs=[0 for i in range(s_size)]
    if t_size>s_size:
        return rs
    for i in range(t_size-1,s_size):
        if i==t_size-1 and s[0:i+1]==t:
            rs[i]=1
            continue
        if s[i-t_size+1:i]+s[i]==t:
            rs[i]=rs[i-1]+1
            continue
        rs[i]=rs[i-1]
    for i in range(s_size):
        print(rs[i],end=' ')
if __name__=='__main__':
    s=input()
    t=input()
    solution(s,t)
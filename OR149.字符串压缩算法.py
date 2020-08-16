'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-14 15:25:39
LastEditors: Liang Anqing
LastEditTime: 2020-08-14 15:34:54
'''
'''
题目描述
复制代码
1
2
3
4
	
输入一串字符，请编写一个字符串压缩程序，将字符串中连续出现的重复字母进行压缩，并输出压缩后的字符串。
例如：
aac 压缩为 1ac
xxxxyyyyyyzbbb 压缩为 3x5yz2b

输入描述:

任意长度字符串

输出描述:

压缩后的字符串

示例1
输入
复制

xxxxyyyyyyzbbb

输出
复制

3x5yz2b


'''
def solution(s):
    size=len(s)
    res=''
    if size<=1:
        return s
    i=0
    while i<size:
        count=0
        while i+1<size and s[i]==s[i+1]:
            count+=1
            i+=1
        if count>0:
            res+=str(count)+s[i]
        else:
            res+=s[i]
        i+=1
    return res
if __name__=='__main__':
    s=input()
    print(solution(s))
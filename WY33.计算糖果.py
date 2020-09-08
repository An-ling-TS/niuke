'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-05 14:57:06
LastEditors: Liang Anqing
LastEditTime: 2020-09-05 15:06:44
'''
'''
题目描述
A,B,C三个人是好朋友,每个人手里都有一些糖果,我们不知道他们每个人手上具体有多少个糖果,但是我们知道以下的信息：
A - B, B - C, A + B, B + C. 这四个数值.每个字母代表每个人所拥有的糖果数.
现在需要通过这四个数值计算出每个人手里有多少个糖果,即A,B,C。这里保证最多只有一组整数A,B,C满足所有题设条件。
输入描述:

输入为一行，一共4个整数，分别为A - B，B - C，A + B，B + C，用空格隔开。 范围均在-30到30之间(闭区间)。

输出描述:

输出为一行，如果存在满足的整数A，B，C则按顺序输出A，B，C，用空格隔开，行末无空格。 如果不存在这样的整数A，B，C，则输出No

示例1
输入
复制

1 -2 3 4

输出
复制

2 1 3

'''
def solution(arr):
    if (arr[0]+arr[2])%2==1 or (arr[1]+arr[3])%2==1:
        print('No')
        return
    a=int((arr[0]+arr[2])/2)
    b=int((arr[1]+arr[3])/2)
    c=arr[3]-b
    if a>=0 and b>=0 and c>=0:
        print(a,end=' ')
        print(b,end=' ')
        print(c,end=' ')
        return
    print('No')
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    solution(arr)
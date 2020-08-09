'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-09 16:32:37
LastEditors: Liang Anqing
LastEditTime: 2020-08-09 16:38:29
'''
'''
题目描述
在你面前有一个n阶的楼梯，你一步只能上1阶或2阶。
请问计算出你可以采用多少种不同的方式爬完这个楼梯。
输入描述:

一个正整数n(n<=100)，表示这个楼梯一共有多少阶

输出描述:

一个正整数，表示有多少种不同的方式爬完这个楼梯

示例1
输入
复制

5

输出
复制

8

'''
def solution(n):
    dp1=1
    dp2=2
    if n<=2:
        return n
    i=2
    while i<n:
        dp1+=dp2
        i+=1
        if i==n:
            return dp1
        dp2+=dp1
        i+=1
    return dp2
if __name__=='__main__':
    n=int(input())
    print(solution(n))
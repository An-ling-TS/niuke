'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-17 14:52:17
LastEditors: Liang Anqing
LastEditTime: 2020-08-17 14:52:21
'''
#coding=utf-8
import sys 

def solution(n):
    temp=n
    if temp<=9:
        return temp
    while temp>9:
        sum_=0
        s=str(temp)
        size=len(s)
        for i in range(size):
            sum_+=int(s[i])
        temp=sum_
    return temp
if __name__=='__main__':
    n=int(input())
    print(solution(n))
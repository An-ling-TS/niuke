'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-05 15:23:24
LastEditors: Liang Anqing
LastEditTime: 2020-09-05 15:49:53
'''
'''
题目描述

有一个长为n的数组A，求满足0≤a≤b<n的A[b]-A[a]的最大值。

给定数组A及它的大小n，请返回最大差值。
测试样例：

[10,5],2

返回：0

'''
# -*- coding:utf-8 -*-

class LongestDistance:
    def __init__(self):
        super().__init__()
    def getDis(self, A, n):
        # write code here
        temp=0
        for i in range(1,n):
            t=max(A[i:n])-min(A[0:i])
            if t>temp:
                temp=t
        print(temp)
        return temp
if __name__=='__main__':
    so=LongestDistance()
    A=[2676,4662,8383,357,6595]
    n=5
    so.getDis(A,n)
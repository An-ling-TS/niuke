'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-26 17:51:52
LastEditors: Liang Anqing
LastEditTime: 2020-09-26 17:58:33
'''
'''
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count=0
        while n:
            count+=1
            n=(n-1)&n
        return count
so=Solution()
n=int(input())
print(so.NumberOf1(n))
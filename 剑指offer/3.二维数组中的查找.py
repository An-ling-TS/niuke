'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-26 16:39:21
LastEditors: Liang Anqing
LastEditTime: 2020-09-26 16:47:30
'''
'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        ROW=len(array)
        COL=len(array[0])
        col=COL-1
        row=0
        while row<ROW and col>=0:
            if array[row][col]>target:
                col-=1
            elif array[row][col]<target:
                row+=1
            else:
                return True
        return False

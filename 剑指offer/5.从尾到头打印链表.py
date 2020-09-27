'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-26 17:01:12
LastEditors: Liang Anqing
LastEditTime: 2020-09-26 17:15:14
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getNext(self,res,listNode):
        if listNode.next!=None:
            res=self.getNext(res,listNode.next)
        res.append(listNode.val)
        return res
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res=[]
        if listNode!=None:
            res=self.getNext(res,listNode)
        return res
so=Solution()
m=ListNode(0)
n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)
n5=ListNode(5)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
print(so.printListFromTailToHead(n1))
print(so.printListFromTailToHead(m))
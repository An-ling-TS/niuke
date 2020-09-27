'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-26 17:17:38
LastEditors: Liang Anqing
LastEditTime: 2020-09-26 17:43:22
'''
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        print('***************')
        print(pre)
        print(tin)
        if len(pre)==0 or len(tin)==0:
            return
        root=TreeNode(pre[0])
        if len(pre)==1 or len(tin)==1:
            return root
        root_index_p=tin.index(pre[0])
        max_index=0
        leftTree=tin[0:root_index_p]
        for i in leftTree:
            if max_index<pre.index(i):
                max_index=pre.index(i)
        root.left=self.reConstructBinaryTree(pre[1:(max_index+1)],tin[0:root_index_p])
        root.right=self.reConstructBinaryTree(pre[max_index+1:len(pre)],tin[root_index_p+1:len(tin)])
        return root
so=Solution()
pre=[1,2,4,7,3,5,6,8]
tin=[4,7,2,1,5,3,8,6]
head=so.reConstructBinaryTree(pre,tin)
print(head.val)
def show(head):
    if head==None:
        return
    show(head.left)
    show(head.right)
    print(head.val)           
show(head)
        
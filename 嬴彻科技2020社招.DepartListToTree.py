'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-08 15:12:51
LastEditors: Liang Anqing
LastEditTime: 2020-09-08 16:27:26
'''
'''
Convert the department list to preorder traversal of the name of department tree

输入例子1:

[["d1", "d0", "IT"], ["d2", "d0", "RD"], ["d0", "", "The Company"], ["d3", "d0", "HR"]]


输出例子1:

["The Company","HR","IT","RD"]


例子说明1:

On each level of the department tree, departments are listed in alphabetical order of the name

'''
class Node:
    def __init__(self,parent,val):
        self.val=val
        self.parent=parent
        self.children=[]
        if parent:
            self.parent.children.append(self)
class Solution:
    def preorder(self,root):
        stack=[]
        stack.append(root)
        rs=[]
        while len(stack)>0:
            cur=stack.pop(0)

            rs.append(cur.val)
            for i in cur.children:
                stack.append(i)
        print(rs)
    def listToTree(self , departments ):
        de=eval(departments)
        de=sorted(de)
        print(de)
        count=len(de)
        temp=dict()
        root=Node(None,de[0][2])
        temp[de[0][0]]=root
        for i in range(count):
            if de[i][1] in temp:
                node=Node(temp[de[i][1]],de[i][2])
                temp[de[i][0]]=node
        self.preorder(root)
        
if __name__=='__main__':
    s=input()
    so=Solution()
    so.listToTree(s)

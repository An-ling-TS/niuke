'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-17 15:10:28
LastEditors: Liang Anqing
LastEditTime: 2020-08-17 15:30:02
'''
class Node():
    val=0
    left=None
    right=None
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n0=Node(0)
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n8=Node(8)
n9=Node(9)

n0.left=n1
n0.right=n2
n1.left=n3
n1.right=n4
n2.left=n5
n2.right=n6
n6.right=n9
n5.left=n8
n3.left=n7

def so(root):
    cur=root
    if cur!=None:
        so(cur.left)
        so(cur.right)
        print(cur.val)
so(n0)
print('--------------------')
def so1(root):
    cur=root
    if cur==None:
        return
    so1(cur.left)
    so1(cur.right)
    print(cur.val)
so1(n0)
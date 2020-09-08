'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-20 16:57:21
LastEditors: Liang Anqing
LastEditTime: 2020-08-20 17:03:37
'''

class Solution:
    def __init__(self):
        pass
    def operate(self , arr1 , arr2 ):
        arr1+=arr2
        del arr1[len(arr1)-2]
        return arr1
if __name__=='__main__':
    arr1=list(map(int,input().strip().split()))
    arr2=list(map(int,input().strip().split()))
    so=Solution()
    print(so.operate(arr1,arr2))

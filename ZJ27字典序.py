'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-13 13:51:35
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-13 14:10:19
'''
def dicOrder(n,m):
    temp=[str(i) for i in range(1,n+1)]
    temp=sorted(temp)
    print(temp)
    return temp[m-1]
n, m = list(map(int, input().strip().split(' ')))
print(dicOrder(n, m))
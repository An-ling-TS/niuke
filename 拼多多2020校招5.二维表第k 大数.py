'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-07 16:54:18
LastEditors: Liang Anqing
LastEditTime: 2020-09-07 17:18:32
'''
'''
]二维表第k大数

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M
在一块长为n，宽为m的场地上，有n✖️m个1✖️1的单元格。每个单元格上的数字就是按照从1到n和1到m中的数的乘积。具体如下

n = 3, m = 3
1   2   3
2   4   6
3   6   9

给出一个查询的值k，求出按照这个方式列举的的数中第k大的值v。
例如上面的例子里，
从大到小为(9, 6, 6, 4, 3, 3, 2, 2, 1)
k = 1, v = 9
k = 2, v = 6
k = 3, v = 6
...
k = 8, v = 2
k = 9, v = 1

输入描述:

只有一行是3个数n, m, k 表示场地的宽高和需要查询的k。使用空格隔开。


输出描述:

给出第k大的数的值。


输入例子1:

3 3 4


输出例子1:

4

'''
def solution(arr):
    n,m,k=arr
    rs=n*m
    for i in range(k-1):
        rs=n*m
        if (n-1)*m>n*(m-1):
            n-=1
        else:
            m-=1  
    print(rs)
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    solution(arr)
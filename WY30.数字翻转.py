'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-08-09 16:13:29
LastEditors: Liang Anqing
LastEditTime: 2020-08-09 16:23:53
'''
'''
题目描述
对于一个整数X，定义操作rev(X)为将X按数位翻转过来，并且去除掉前导0。例如:
如果 X = 123，则rev(X) = 321;
如果 X = 100，则rev(X) = 1.
现在给出整数x和y,要求rev(rev(x) + rev(y))为多少？
输入描述:

输入为一行，x、y(1 ≤ x、y ≤ 1000)，以空格隔开。

输出描述:

输出rev(rev(x) + rev(y))的值

示例1
输入
复制

123 100

输出
复制

223

'''
def rev(arr):
    x=int(str(arr[0])[::-1])
    y=int(str(arr[1])[::-1])
    return int(str(x+y)[::-1])
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    print(rev(arr))
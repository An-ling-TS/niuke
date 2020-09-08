'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-07 16:09:52
LastEditors: Liang Anqing
LastEditTime: 2020-09-07 16:42:23
'''
'''
[编程题]多多的排列函数

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 256M，其他语言512M
数列 {An} 为N的一种排列。
例如N=3，可能的排列共6种：
复制代码
1
2
3
4
5
6
	
1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1
定义函数F:

其中|X|表示X的绝对值。

现在多多鸡想知道，在所有可能的数列 {An} 中，F(N)的最小值和最大值分别是多少。

输入描述:

第一行输入1个整数T，表示测试用例的组数。
( 1 <= T <= 10 )
第二行开始，共T行，每行包含1个整数N，表示数列 {An} 的元素个数。
( 1 <= N <= 100,000 )


输出描述:

共T行，每行2个整数，分别表示F(N)最小值和最大值


输入例子1:

2
2
3


输出例子1:

1 1
0 2


例子说明1:

对于N=3：
- 当{An}为3，2，1时可以得到F(N)的最小值0
- 当{An}为2，1，3时可以得到F(N)的最大值2

'''
'''
1.N累加和为偶数时最小值0，N累加和为奇数时最小值1
2.F(N)的最大值为min(F(N-1))-N

'''
def solution(t,arr):
    rs=[]
    temp=[]
    max_t=max(arr)
    sum_t=1
    for i in range(1,max_t+1):
        if i==1:
            temp.append([1,1])
            continue
        sum_t+=i
        if sum_t%2==0:
            temp.append([0,abs(min(temp[i-2])-i)])
        else:
            temp.append([1,abs(min(temp[i-2])-i)])
    for i in range(t):
        print(temp[arr[i]-1][0],end=' ')
        print(temp[arr[i]-1][1])

            
if __name__=='__main__':
    t=int(input())
    arr=[]
    for i in range(t):
        arr.append(int(input()))
    solution(t,arr)
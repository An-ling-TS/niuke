'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-21 16:13:57
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-21 16:14:35
'''
'''
题目描述

小爱有一个奇怪的计数器。在第一个时刻计数器显示数字3，在接下来的每一个时刻，屏幕上的数字都会减1，直到减到1为止。
接下来，计数器会重置为上一个计数周期初始值的两倍，然后再每一个时刻减1。具体过程如下图所示：

找出规律，并打印出t时刻计数器的值。
输入描述:

输入为时刻t，一个整形数字。0<t<1e12

输出描述:

计数器显示的值。

示例1
输入
复制

4

输出
复制

6


'''
def solution(t):
    i=1
    while True:
        if t>i*3:
            i=i*2+1
            continue
        return i*3+1-t
        
if __name__=='__main__':
    t=int(input())
    print(solution(t))
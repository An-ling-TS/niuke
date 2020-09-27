'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-20 20:41:17
LastEditors: Liang Anqing
LastEditTime: 2020-09-20 20:47:32
'''
'''
链接：https://ac.nowcoder.com/acm/contest/7413/E
来源：牛客网

题目描述
二维平面的第一象限内有 n 条线段，其斜率均为 1 或 -1。保证相同斜率的线段无交（含端点）。
有 m 次询问，每次从一个位置释放一个小球，小球可以视为一个点。小球会下落（即朝着 y 坐标减小的方向），分为三种情况：
    1. 当小球不与任何线段重合或者位于恰好一条线段的下端点时，竖直向下移动。
    2. 当小球在恰好一条线段上（不含下端点），沿着该线段向下移动。
    3. 当小球与两条线段重合时（位于交叉点上），停止运动。
对于每个询问，你需要求出小球是否会在有限时间内停止运动。
输入描述:

第一行两个整数 n,m。

接下来 n 行，第 i 行三个正整数 ai,bi,cia_i,b_i,c_iai​,bi​,ci​，表示第 i 条线段的上端点坐标是 (ai,bi)(a_i,b_i)(ai​,bi​)，下端点的坐标是 (ci,bi−∣ai−ci∣)(c_i,b_i-|a_i-c_i|)(ci​,bi​−∣ai​−ci​∣)。保证相同斜率的线段无交（含端点）。

接下来 m 行，第 i 行两个正整数 xi,yix_i,y_ixi​,yi​，表示第 i 次询问的小球初始坐标是 (xi,yi)(x_i,y_i)(xi​,yi​)。

输出描述:

一行长为 m 的字符串，第 i 位是 1 表示第 i 次询问时小球不会停止，0 表示会停止。

示例1
输入
复制

6 6
1 2 2
2 3 4
3 3 2
4 3 5
4 5 3
5 2 4
1 2
2 2
2 3
4 5
5 2
5 4

输出
复制

110000
'''
def solution(n,m,lines,pos):
    print(lines)
    lines=sorted(lines)
    print(lines)
    res=''
    stop=[]
    
if __name__=='__main__':
    n,m=list(map(int,input().strip().split()))
    lines=[]
    pos=[]
    for i in range(n):
        a,b,c=list(map(int,input().strip().split()))
        lines.append([a,b,c,b-abs(a-c)])
    for i in range(m):
        pos.append(list(map(int,input().strip().split())))
    print(solution(n,m,lines,pos))
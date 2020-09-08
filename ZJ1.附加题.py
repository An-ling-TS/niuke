'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-05 15:51:57
LastEditors: Liang Anqing
LastEditTime: 2020-09-05 16:09:01
'''
'''
题目描述
存在n+1个房间，每个房间依次为房间1 2 3...i，每个房间都存在一个传送门，i房间的传送门可以把人传送到房间pi(1<=pi<=i),现在路人甲从房间1开始出发(当前房间1即第一次访问)，每次移动他有两种移动策略：
    A. 如果访问过当前房间 i 偶数次，那么下一次移动到房间i+1；
    B. 如果访问过当前房间 i 奇数次，那么移动到房间pi；
现在路人甲想知道移动到房间n+1一共需要多少次移动；
输入描述:

第一行包括一个数字n(30%数据1<=n<=100，100%数据 1<=n<=1000)，表示房间的数量，接下来一行存在n个数字 pi(1<=pi<=i), pi表示从房间i可以传送到房间pi。

输出描述:

输出一行数字，表示最终移动的次数，最终结果需要对1000000007 (10e9 + 7) 取模。

示例1
输入
复制

2
1 2

输出
复制

4

说明

开始从房间1 只访问一次所以只能跳到p1即 房间1， 之后采用策略A跳到房间2，房间2这时访问了一次因此采用策略B跳到房间2，之后采用策略A跳到房间3，因此到达房间3需要 4 步操作。

'''
def solution(n,p):
    visit=[False for i in range(n+1)]
    cur=1
    visit[0]=True
    rs=0
    while cur!=n+1:
        if not visit[cur-1]:
            cur+=1
        else:
            cur=p[cur-1]
        visit[cur-1]=not visit[cur-1]
        rs+=1
    return rs
if __name__=='__main__':
    n=int(input())
    p=list(map(int,input().strip().split()))
    print(solution(n,p))
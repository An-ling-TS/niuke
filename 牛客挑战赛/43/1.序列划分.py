'''
链接：https://ac.nowcoder.com/acm/contest/7413/A
来源：牛客网

给出一个长为 n 的序列 A1,A2,…,AnA_1, A_2, \dots, A_nA1​,A2​,…,An​。
你需要将序列 A 划分成若干个连续段，一段的权值定义为这段内的所有数的按位或。
你需要恰当地选择划分方案，使得每段的权值之和最大。
求出每段的权值之和的最大值。
输入描述:

第一行一个整数 n。
接下来一行 n 个整数 A1,A2,…,AnA_1, A_2, \dots, A_nA1​,A2​,…,An​。

输出描述:

一个整数，表示答案。

示例1
输入
复制

3
9 6 16

输出
复制

31

说明

一种最优的方案是划分成 (9,6) (16)。

备注:

1≤n≤1051 \le n \le 10^51≤n≤105，0≤Ai≤1090 \le A_i \le 10^90≤Ai​≤109。
'''
def solution(n,arr):
    dp=[arr[i] for i in range(n)]
    res=0
    for i in range(0,n):
        if res|arr[i]>=arr[i]+res:
            res=res|arr[i]
        else:
            res+=arr[i]
    return res
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    print(solution(n,arr))
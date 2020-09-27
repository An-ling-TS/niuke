'''
链接：https://ac.nowcoder.com/acm/contest/7413/B
来源：牛客网

题目描述
有一个集合 S，初始为 {1,2,3,…,n}\{1, 2, 3, \dots, n\}{1,2,3,…,n}。
接下来会进行若干次操作，每次操作如下：
    选择一个整数 x∈Sx \in Sx∈S，满足 S 中小于 x 的元素不超过 m 个。然后在 S 中删除 x。
求出通过以上操作能够得到多少种不同的集合 S 。
答案对 998244353 取模。
输入描述:

一行两个整数 n, m。

输出描述:

一个整数，表示答案。

示例1
输入
复制

3 1

输出
复制

7

说明

除了 {1, 2} 之外，其他 {1, 2, 3} 的子集都能得到。

备注:

1≤n≤1051 \le n \le 10^51≤n≤105，0≤m<n0 \le m < n0≤m<n。
'''
def solution(n,m):
    pass
if __name__=='__main__':
    n,m=list(map(int,input().strip().split()))
    print(solution(n,m))
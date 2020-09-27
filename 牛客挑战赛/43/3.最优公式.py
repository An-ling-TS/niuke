'''
Descripttion: 
version: 
Author: Liang Anqing
Date: 2020-09-20 20:27:26
LastEditors: Liang Anqing
LastEditTime: 2020-09-20 20:28:54
'''
'''
链接：https://ac.nowcoder.com/acm/contest/7413/C
来源：牛客网

题目描述
有一个长为 n 的数组 A1,A2,…,AnA_1, A_2, \dots, A_nA1​,A2​,…,An​。
你需要找到两个实数 a, b，使得 ∑i=1n∑j=1nmax⁡(∣Ai−a∣,∣Aj−b∣)\sum_{i=1}^n \sum_{j=1}^n \max (|A_i - a|, |A_j - b|)∑i=1n​∑j=1n​max(∣Ai​−a∣,∣Aj​−b∣) 尽可能小。
求出这个最小值。
容易发现答案乘上 2 一定是整数，求出答案乘上 2 模 109+710^9 + 7109+7 的值。
输入描述:

第一行一个整数 n。
接下来一行 n 个整数 A1,A2,…,AnA_1, A_2, \dots, A_nA1​,A2​,…,An​。

输出描述:

输出一个整数，表示答案乘上 2 模 109+710^9 + 7109+7 的值。

示例1
输入
复制

2
1 2

输出
复制

4

说明

a=b=32a = b = \frac{3}{2}a=b=23​ 时最优。
'''
def solution(n,arr):
    a=sum(arr)/n
    
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    print(solution(n,arr))
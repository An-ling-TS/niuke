'''
题目描述
n 只奶牛坐在一排，每个奶牛拥有 ai 个苹果，现在你要在它们之间转移苹果，使得最后所有奶牛拥有的苹果数都相同，每一次，你只能从一只奶牛身上拿走恰好两个苹果到另一个奶牛上，问最少需要移动多少次可以平分苹果，如果方案不存在输出 -1。
输入描述:

每个输入包含一个测试用例。每个测试用例的第一行包含一个整数 n（1 <= n <= 100），接下来的一行包含 n 个整数 ai（1 <= ai <= 100）。

输出描述:

输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出 -1。

示例1
输入
复制

4
7 15 9 5

输出
复制

3

'''
def solution(n,arr):
    total=sum(arr)
    if total%n>0:
        return -1
    per=total/n
    res=0
    for i in range(n):
        if arr[i]%2!=per%2:
            return -1
        if arr[i]<per:
            res+=(per-arr[i])/2
    return int(res)
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    print(solution(n,arr))
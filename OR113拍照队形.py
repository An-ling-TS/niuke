'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-31 17:20:51
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-31 17:50:37
'''
'''
题目描述
猿辅导公司的 N位（N>=4）研发同学组织了一次秋游活动，某同学带了个无人机在高空拍照，活动结束时，先拍了一张所有同学排成公司猴头Logo的照片， 接着有人提议再排成“猿”的首字母Y字形来拍一张合照。

用字符串中的每一个字符（不是换行符或结束符'\0'）代表一位老师，输出排好后的队形。要求 Y字除去中心点外，上下半部分等高，按照从左到右，从上到下进行排序。队形中没人的部分用空格占位。
输入数据保证可以排出一个完整的Y字，即长度为 3k+1 （k>=1）

例如: 7个 x ，排成队形为（为了方便说明，这里用‘-’代替空格）：
x---x
-x-x
--x
--x
--x

// 参考程序
#include <cstring>
#include <iostream>
#include <cstdio>
using namespace std;
char str[1010];
int N;
int main(){
    scanf("%d\n", &N);
    // TODO: 读入字符串，注意可能含空格

    // TODO: 输出拍照队形，没人用空格占位
    printf(" %c\n", str[0]);
}

	


输入描述:

输入数据有两行，第一行输入N(N<=1000)，表示字符串长度。
第二行输入字符串。

输出描述:

用字符串表示的排好的队形，没人处用空格（' '）占位，行尾不能有多余字符，即每行最后一个字符（除了换行符以外），为字符串中代表该老师的字符。

示例1
输入
复制

4
a3f/

输出
复制

a 3
 f
 /

示例2
输入
复制

7
abcdefg

输出
复制

a   b
 c d
  e
  f
  g

示例3
输入
复制

10
iiiiiiiiii

输出
复制

i     i
 i   i
  i i
   i
   i
   i
   i

'''
def solution(n,arr):
    l=int((n-1)/3)
    m=2*l+1
    i=0
    d=0
    while i<n:
        if i<l*2:
            k=0
            while k<d:
                print('-',end='')
                k+=1
            print(arr[i],end='')
            i+=1
            while k<m-2-d:
                print('-',end='')
                k+=1
            print(arr[i])
            i+=1
            d+=1
        else:
            for r in range(l):
                print('-',end='')
            print(arr[i])
            i+=1
if __name__=='__main__':
    n=int(input())
    s=input()
    solution(n,s)
'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-19 21:42:26
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-19 21:45:38
'''
def get_grade(grade):
    grade[0]=
def solution(grades):
    for key,vals in grades.items():
        total_grade=(vals[0]+vals[1]+vals[2])*0.25+(vals[3]+vals[4])*0.5
        grades[key]=total_grade
    res=sorted(grades.items(),key=lambda d:d[1])
    for key,vsl in res:
        print(key+str(res))
if __name__=='__main__':
    n=int(input())
    grades=dict()
    for i in range(n):
        arr=input().strip().split()
        grades[arr[0]]=list(map(int,arr[1:len(arr)]))
    solution(grades)
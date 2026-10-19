# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X=map(int,input().split())
marks=[]
for i in range(X):
    marks.append(list(map(float,input().split())))
for student_marks in zip(*marks):
    print(sum(student_marks) / X)

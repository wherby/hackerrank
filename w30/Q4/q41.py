filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)




num,k= map(int , ins[0].strip().split())
index=1
ls =[]
hight=[]
weight=[]
A=[0]*num
B=[0]*num
F=[0]*num
dp=[]
v=[]
for i in range(num):
	dp.append([0]*num)
	v.append([0]*num)
for i in range(num):
	h,n= map(int , ins[index+i].strip().split())
	hight.append(h)
	weight.append(n)

for i in range(num):
	for j in range(i+1,num):
		v[i][j] = v[i][j-1] + weight[j]


print hight,weight,dp,A,B
	

	
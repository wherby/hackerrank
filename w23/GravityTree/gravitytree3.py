filename = "input/input00.txt"
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



	
#[level, parent-list]
n, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())
dic={}
vt=[1]
pl=[0]*(n+1)
for i in range(n+1):
	pl[i]=[]
for i in range(n-1):
	t=ls[i]
	pl[t].append(i+2)
print pl
for i in range(n+1):
	for j in pl[i]:
		

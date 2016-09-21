filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import copy
from collections import deque

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
pvl=[0]*(n+1)
for i in range(n+1):
	pl[i]=[]
for i in range(n-1):
	t=ls[i]
	pl[t].append(i+2)
for i in range(n):
	tp=pl[i+1]
	for j in tp:
		pvl[j]=i+1
print pl
print pvl


dicLen={}

def dfsTreeLCA(pl,dicLen):
	plt=copy.deepcopy(pl)
	ving=set([1])
	ved=set()
	pstak=[1]
	while len(pstak)!=0:
		t=pstak[-1]
		if len(plt[t])!=0:
			x1=plt[t][0]
			plt[t]=plt[t][1:]
			ving.add(x1)	
			pstak.append(x1)
		else:
			ved.add(t)
			pstak.pop()
	print ving
	print ved


dfsTreeLCA(pl,dicLen)
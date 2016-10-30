filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin
CONSTPRIME = 1000000007

ins=[]
for line in inputA:
    ins.append(line)

fibList=[]
fibList.append(1)
fibList.append(1)
k=2
for i in range(1000000):
	x= fibList[k+i -2] + fibList[k+i-1]
	fibList.append(x)

t1= map(lambda x: x%CONSTPRIME,fibList)
x = filter(lambda x: x ==0,t1)
print len(x)


def getRange(i,j):
	re= j*(j+1)/2 - i * (i-1)/2
	return re

def genLSS(ls):
	ls = sorted(ls)
	n =len(ls)
	pars=[]
	for i in range(n):
		for j in range(i,n):
			pars.append(getRange(ls[i],ls[j]))
	return sorted(pars)

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i*2].strip().split())
	ls= map(int , ins[index+i*2+1].strip().split())
	print genLSS(ls)
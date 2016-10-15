filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin

def PowerSum(k,n):
	if k ==1:
		return n*(n+1)/2
	if k ==2:
		return n*(n+1)*(2*n+1)/6
	if k==3:
		return n**2 *(n+1)**2 /4
	if k ==4:
		return n *(n+1) *(2*n +1) *(3*n**2 +3*n -1) /30
	if k ==5:
		return 


ins=[]
for line in inputA:
    ins.append(line)


CONSTPRIME = 1000000007

def getAre(ls,ed):
	re =[]
	for i in ls:
		for j in range(1,ed/i +1):
			if j *i != ed:
				re.append(j*i)
	re.append(ed)
	return re

def exponen(base,exponent):
	global CONSTPRIME
	if base == 1:
		return 1
	result =1
	while exponent >0:
		if exponent &1:
			result=result *base 
		exponent =exponent >>1
		base =base **2 %CONSTPRIME
	return result


def calcArr(re):
	global st,expon,CONSTPRIME
	rs=0
	for i in re:
		t = exponen(i,expon)
		rs = rs +t
	return rs % CONSTPRIME



q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,expon,ed= map(int , ins[index+i*2].strip().split())
	st =1
	re = [x for x in range(st,ed+1)]
	ls= map(int , ins[index+i*2 +1].strip().split())
	re2= set(getAre(ls,ed))
	re = filter(lambda x: x not in re2, re)
	print calcArr(re)
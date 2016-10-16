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

Map1=[]
cn=0
for i in range(9):
	for j in range(i+1,9):
		t1 = [0]*9
		t1[i]=1
		t1[j]=1
		t1=map(str,t1)
		t2="".join(t1)
		Map1.append(t2)
print Map1
trans={}
for i in Map1:
	stat= i[:6]
	tras1=i[3:]
	if stat not in trans:
		trans[stat] = [tras1]
	else:
		trans[stat].append(tras1)
print trans



def getNum(m):
	global Map1,trans





q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	m,n= map(int , ins[index+i].strip().split())
	
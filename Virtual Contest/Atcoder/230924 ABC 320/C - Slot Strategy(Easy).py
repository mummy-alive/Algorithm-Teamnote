M=int(input())
S=[]

for i in range(3):
    S.append(input()*3)
Ans=[]

import itertools
for s in range(10):
    s=str(s)
    if s in S[0] and s in S[1] and s in S[2]:
        for i,j,k in itertools.permutations([0,1,2],3):
            a=S[i].index(s)
            a+=1+S[j][a+1:].index(s)
            a+=1+S[k][a+1:].index(s)
            Ans.append(a)

if len(Ans):
    print(min(Ans))
else:
    print(-1)

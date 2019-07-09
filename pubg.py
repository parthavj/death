d=int(input())
v=[]
for n in range(0,d):
 lan=input()
 v.append(lan)
thissss=[]
for n in zip(*v):
 if(n.count(n[0])==len(n)):
  thissss.append(n[0])
 else:
  break
print(''.join(thissss))

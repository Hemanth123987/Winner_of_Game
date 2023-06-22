st1=input()

s=list(st1)

v=["a","e","i","o","u"]
l=[]
l2=[]
j=0
n=0
p=0
for i in s:
    if i in v:
        for k in range(len(st1)+1):
            l.append(st1[p:k])
        
    elif i not in v:
        for m in range(len(st1)+1):
            l2.append(st1[p:m])
        
    p=p+1

ajay=[]
raj=[]
for i in l:
    if i!=" ":
        ajay.append(len(set(i)))
for i in l2:
    if i!=" ":
        raj.append(len(set(i)))
sum_ajay=0
for i in ajay:
    sum_ajay=i+sum_ajay
sum_raj=0
for i in raj:
    sum_raj=i+sum_raj
if sum_ajay>sum_raj:
    print("Ajay"+" "+str(sum_ajay))
else:
    print("Raj"+" "+str(sum_raj))
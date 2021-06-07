N=int(input())
Dtbl=list()
for i in range(N):
    a=input()
    Dtbl.append(a)

Dtbl.sort(key=lambda x : (len(x),x))

print(Dtbl[0])
for i in range(1,N):
    if Dtbl[i-1] != Dtbl[i] :
        print(Dtbl[i])


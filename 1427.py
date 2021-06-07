N=input()

Nlist = list(N)
Nlist.sort(reverse=True)
for i in range(len(Nlist)):
    print(Nlist[i], end='')

N= int(input())
DTbl=list()
for i in range(N):
    a = list(map(int, input().split()))
    DTbl.append(a)
# print(DTbl)
DTbl.sort(key=lambda x:(x[1],x[0]))

for i in range(N):
    print(DTbl[i][0], DTbl[i][1])

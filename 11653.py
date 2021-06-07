ans = list()
N=int(input())
if N == 1:
    exit()
i = 2
while i <= N:
    if N % i == 0:
        N= N//i
        ans.append(i)
        if N == 1:
            break
        i = 2
    else:
        i += 1
print(*ans,end='\n')
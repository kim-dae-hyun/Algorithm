
def calculater_num(result, oprt, index):
    global maxnum, minnum
    if oprt == 0:
        result += numlist[index]
    elif oprt == 1:
        result -= numlist[index]
    elif oprt == 2:
        result *= numlist[index]
    elif oprt == 3:
        result = int(result / numlist[index])
   
    oprtcntlist[oprt] -= 1 
    if index + 1 == N:
        maxnum = max(maxnum, result)
        minnum = min(minnum, result)        
        return

    for i in range(4):
        if oprtcntlist[i] > 0:
            calculater_num(result, i, index + 1)
            oprtcntlist[i] += 1 
            
N = int(input())
numlist = list(map(int, input().split()))
oprtcntlist = list(map(int, input().split()))

maxnum = -1000000000
minnum = 1000000000

for i in range(4):
    if oprtcntlist[i] > 0:
        calculater_num(numlist[0], i, 1)
        oprtcntlist[i] += 1 

print(maxnum)
print(minnum)

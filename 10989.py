import sys
DataTble = [0]* 10001
# print(DataTble)

N = int(input())
listdata = list()
for i in range(N):
    DataTble[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(DataTble[i]):
        sys.stdout.write(str(i) + '\n')

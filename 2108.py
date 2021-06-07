import sys
import statistics
DataTable = list()
N = int(input())
listdata = list()
for i in range(N):
    DataTable.append(int(sys.stdin.readline()))

print(round(statistics.mean(DataTable)))
print(statistics.median(DataTable))
modeval = statistics.multimode(DataTable)
if len(modeval) > 1:
    modeval.sort()
    print(modeval[1])
else:
    print(modeval[0])

print(max(DataTable) - min(DataTable))


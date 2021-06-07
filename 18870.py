import sys
input = sys.stdin.readline

N = int(input())
coor = list(map(int, input().split()))
tmpCoor = list(sorted(set(coor)))

dic = {value : index for index, value in enumerate(tmpCoor)}

for element in coor:
    print(dic[element], end = ' ')








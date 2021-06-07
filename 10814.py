n = int(input())
data = list()
for i in range(n):
    age, name = input().split()
    data.append([int(age),name])

data = sorted(data, key = lambda x: (x[0]))
for i in range(len(data)):
    print(data[i][0], data[i][1])

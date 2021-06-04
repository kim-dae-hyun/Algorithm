def calculate_leve():
    global difflevel
    teamA = 0
    teamB = 0
    for i in range(N):
        for j in range(i+1,N):
            if (i in teamdata) and (j in teamdata):
                teamA += (datatable[i][j] + datatable[j][i])
            elif (i not in teamdata) and (j not in teamdata):
                teamB += (datatable[i][j] + datatable[j][i])
    difflevel = min(difflevel, abs(teamA - teamB))

def make_team(index):
    teamdata.append(index)
    if len(teamdata) == N/2:
        calculate_leve()
        return

    for i in range(index+1, N):
        make_team(i)
        teamdata.pop()

N = int(input())
datatable = list()
teamdata = list()
difflevel = 20000
for i in range(N):
    a = list(map(int, input().split()))
    datatable.append(a)

for i in range((N//2) + 1):
    make_team(i)
    teamdata.pop()

print(difflevel)
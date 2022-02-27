from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
graph = []
data = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    # 바이러스의 상태 저장
    for j in range(N):
        if graph[i][j] != 0:
            # 바이러스의 종류, 시간, 위치
            data.append((graph[i][j],0,i,j))
S, X, Y = map(int, input().split())

'''
data = [(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)]
'''
data.sort()
q = deque(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    v, t, x, y = q.popleft()
    if t == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                q.append((graph[nx][ny],t+1,nx,ny))
    
print(graph[X-1][Y-1])
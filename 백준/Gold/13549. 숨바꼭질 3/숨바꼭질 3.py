from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10**5
visited = [0] * (MAX+1)

def bfs(i, j):
    q = deque([i])
    visited[i] = 1
    while q:
        x = q.popleft()
        if x == j:
            return
        for nx in (x * 2, x - 1, x + 1):
            if nx < 0 or nx > MAX: continue
            if visited[nx]: continue
            if nx == x * 2: visited[nx] = visited[x]
            else: visited[nx] = visited[x] + 1      
            q.append(nx)

bfs(N, K)
print(visited[K] - 1)
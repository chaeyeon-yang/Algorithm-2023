from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

# 그래프 연결
for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
q.append(1)

visited = [0]*(N+1)

def bfs():
  while q:
    now = q.popleft()
    for nxt in graph[now]:
      if not visited[nxt]:
        visited[nxt] = now
        q.append(nxt)
    print(q)
    print(visited)

bfs()
res = visited[2:]
for i in res:
  print(i)
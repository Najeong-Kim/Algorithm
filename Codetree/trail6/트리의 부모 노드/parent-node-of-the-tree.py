from collections import deque

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

tree = {}
for edge in edges:
    a, b = edge
    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]
    if b in tree:
        tree[b].append(a)
    else:
        tree[b] = [a]

parents = [0] * (n + 1)
parents[1] = 1
dq = deque([1])
while len(dq):
    now = dq.popleft()
    for node in tree[now]:
        if not parents[node]:
            parents[node] = now
            dq.append(node)

for i in range(2, n + 1):
    print(parents[i])


# Please write your code here.
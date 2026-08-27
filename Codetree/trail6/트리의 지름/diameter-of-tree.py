import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
lists = [[] for _ in range(n + 1)]

for edge in edges:
    a, b, c = edge
    lists[a].append([b, c])
    lists[b].append([a, c])

def find_far_node(start):
    visited = [False] * (n + 1)
    max_node, max_distance = 0, 0
    visited[start] = True

    def dfs(now, distance):
        nonlocal max_node
        nonlocal max_distance
        nonlocal visited

        for node in lists[now]:
            this_node, this_distance = node
            if not visited[this_node]:
                if max_distance < distance + this_distance:
                    max_node = this_node
                    max_distance = distance + this_distance
                visited[this_node] = True
                dfs(this_node, distance + this_distance)
    dfs(start, 0)
    return max_node, max_distance

first_node, first_distance = find_far_node(1)
_, result = find_far_node(first_node)

print(result)
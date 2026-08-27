m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]
go_list = {}
come_list = {}
edge_list = []

for edge in edges:
    a, b = edge
    if a in go_list:
        go_list[a].append(b)
    else:
        go_list[a] = [b]

    if b in come_list:
        come_list[b].append(a)
    else:
        come_list[b] = [a]
    
    if a not in edge_list:
        edge_list.append(a)
    if b not in edge_list:
        edge_list.append(b)

is_tree = 1
root = 0

root_count = 0

for edge in edge_list:
    if edge not in come_list.keys():
        root_count += 1
        root = edge
    elif len(come_list[edge]) != 1:
        is_tree = 0

if root_count != 1:
    is_tree = 0

visited = [root]
def dfs(node):
    if node in visited:
        is_tree = 0
    if node not in go_list:
        return
    for go_node in go_list[node]:
        visited.append(go_node)
        dfs(go_node)

if is_tree:
    dfs(root)
if len(edge_list) != len(visited):
    is_tree = 0
print(is_tree)
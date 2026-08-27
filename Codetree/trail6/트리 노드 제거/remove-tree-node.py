n = int(input())
parent = list(map(int, input().split()))
left = [True] * n
remove_node = int(input())

def is_parent(node, target):
    if parent[node] == target:
        return True
    elif parent[node] == -1:
        return False
    return is_parent(parent[node], target)

count = 1
left[remove_node] = False
for i in range(n):
    if is_parent(i, remove_node):
        left[i] = False
        count += 1

parents = [False] * n
for i in range(n):
    if not left[i] or parent[i] == -1:
        continue
    parents[parent[i]] = True

result = 0
for i in range(n):
    if left[i] and not parents[i]:
        result += 1

print(result)
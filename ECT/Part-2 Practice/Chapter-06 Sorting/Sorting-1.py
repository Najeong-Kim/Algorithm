n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

array.sort()
array.reverse()

result = ''

for i in array:
    result += str(i) + ' '

print(result)

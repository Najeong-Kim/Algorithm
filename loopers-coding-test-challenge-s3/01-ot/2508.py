t = int(input())

for _ in range(t):
    input()
    r, c = map(int, input().split())
    candies = [list(input()) for _ in range(r)]

    count = 0

    for i in range(r):
        for j in range(c):
            if i < r - 2:
                if candies[i][j] == 'v' and candies[i + 1][j] == 'o' and candies[i + 2][j] == '^':
                   count += 1
            if j < c - 2:
                if candies[i][j] == '>' and candies[i][j + 1] == 'o' and candies[i][j + 2] == '<':
                   count += 1
    print(count)

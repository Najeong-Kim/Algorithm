# 답이 여러가지인 경우에는 틀릴듯
arr = [int(input()) for _ in range(9)]
arr.sort()

for a in range(9):
    for b in range(a + 1, 9):
        for c in range(b + 1, 9):
            for d in range(c + 1, 9):
                for e in range(d + 1, 9):
                    for f in range(e + 1, 9):
                        for g in range(f + 1, 9):
                            if arr[a] + arr[b] + arr[c] + arr[d] + arr[e] + arr[f] + arr[g] == 100:
                                print(arr[a])
                                print(arr[b])
                                print(arr[c])
                                print(arr[d])
                                print(arr[e])
                                print(arr[f])
                                print(arr[g])
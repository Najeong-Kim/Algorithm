n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

count = 0


def plus(input_list):
    global count
    global m
    global k
    while m != 0:
        for _ in range(k):
            if m != 0:
                count += input_list[-1]
                m = m - 1
            else:
                break
        if m != 0:
            count += input_list[-2]
            m = m - 1
    return count


plus(data)
print(count)

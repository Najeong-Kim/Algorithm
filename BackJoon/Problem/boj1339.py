import sys
input = sys.stdin.readline

N = int(input())
words = {}

for i in range(N):
    word = input().rstrip()
    for j in range(len(word)):
        alphabet = word[len(word) - 1 - j]
        if alphabet in words:
            words[alphabet] += 10 ** j
        else:
            words[alphabet] = 10 ** j

words_list = list(words.items())
words_list.sort(key=lambda x: x[1], reverse=True)

answer = 0
now = 9

for i in words_list:
    answer += i[1] * now
    now -= 1

print(answer)

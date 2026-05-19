N = int(input())
questions = []
for i in range(N):
    number, strike, ball = map(int, input().split())
    questions.append((number, strike, ball))

def checkNumber(real, guess, guess_strike, guess_ball):
    strike = 0
    ball = 0
    for i in range(3):
        if real[i] == guess[i]:
            strike += 1
        elif real[i] == guess[(i + 1) % 3] or real[i] == guess[(i + 2) % 3]:
            ball += 1
    return (strike == guess_strike) and (ball == guess_ball)

count = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i == j) or (j == k) or (k == i):
                continue
            check = 0
            for question in questions:
                number, strike, ball = question
                if (checkNumber(str(i * 100 + j * 10 + k), str(number), strike, ball)):
                    check += 1
            if check == N:
                count += 1

print(count)
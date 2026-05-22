N = int(input())

isPossible = 'NO'
def plus(prev, stage):
    global isPossible
    if N != 0 and prev == N:
        isPossible = 'YES'
        return
    if stage < 0 or prev > N:
        return
    plus(prev + 3 ** stage, stage - 1)
    plus(prev, stage - 1)

plus(0, 20)
print(isPossible)
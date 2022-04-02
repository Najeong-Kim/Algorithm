N = int(input())
total = 0


def check_group_word(word):
    check = word[0]
    checked = [word[0]]
    for i in range(1, len(word)):
        if word[i] == check:
            continue
        else:
            if word[i] in checked:
                return False
            else:
                check = word[i]
                checked.append(word[i])
    return True


for i in range(N):
    if check_group_word(input()):
        total += 1

print(total)

word = input()

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

for alphabet in alphabets:
    while True:
        if alphabet in word:
            word = word.replace(alphabet, "*")
            count += 1
        else:
            break

print(len(word))

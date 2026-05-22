while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    number = 0
    while count != n:
        number += 1
        word_number = str(number)
        if (len(set(word_number)) == len(word_number)):
            count += 1
    print(number)

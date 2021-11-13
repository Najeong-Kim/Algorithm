import copy

T = int(input())


def put_number(number, arr):
    if number == N:
        arr.append(str(number))
        check(arr)
    else:
        arr.append(str(number))
        put_sign(number, arr)


def put_sign(number, arr):
    sign_array = ['+', ' ', '-']
    number += 1
    for sign in sign_array:
        arr_copy = copy.deepcopy(arr)
        arr_copy.append(sign)
        put_number(number, arr_copy)


def check(arr):
    result = ''.join(arr)
    check_text = result.replace(' ', '')
    if int(eval(check_text)) == 0:
        answer_array.append(result)


for _ in range(T):
    N = int(input())
    answer_array = []
    put_number(1, [])
    answer_array.sort()
    for answer in answer_array:
        print(answer)
    print()

n = int(input())

student = []

for _ in range(n):
    student.append(list(map(str, input().split())))

for i in range(n):
    student[i][1] = int(student[i][1])


def setting(data):
    return data[1]


result = sorted(student, key=setting)

answer = ''

for i in range(len(result)):
    answer += result[i][0] + ' '


print(answer)

words = input()

stack = ""

for word in words:
    if word == "(" or word == "[":
        stack += word
    elif word == ")":
        if len(stack) and stack[-1] == "(":
            stack = stack[:-1]
        else:
            stack += word
    elif word == "]":
        if len(stack) and stack[-1] == "[":
            stack = stack[:-1]
        else:
            stack += word

result = []

if len(stack) != 0:
    print(0)
else:
    for word in words:
        if word == "(" or word == "[":
            result.append(word)
        elif word == ")":
            if result[-1] == '(':
                result[-1] = 2
            else:
                result[-1] = result[-1] * 2
                temp = result.pop()
                result.pop()
                result.append(temp)
        elif word == "]":
            if result[-1] == '[':
                result[-1] = 3
            else:
                result[-1] = result[-1] * 3
                temp = result.pop()
                result.pop()
                result.append(temp)
        if len(result) >= 2 and type(result[-1]) is int and type(result[-2]) is int:
            result[-2] = result[-1] + result[-2]
            result.pop()

    print(result[0])

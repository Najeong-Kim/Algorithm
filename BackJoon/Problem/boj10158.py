w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

move_x = t % (w * 2)
move_y = t % (h * 2)


def location(now, move, size):
    if move == 0:
        return now
    elif 0 < move <= (size - now):
        return now + move
    elif (size - now) < move <= (size * 2 - now):
        return size * 2 - now - move
    else:
        return move - size * 2 + now


print(location(p, move_x, w), location(q, move_y, h))

x, y, w, h = map(int, input().split())
min = x
if w - x < min :
    min = w - x
if y < min:
    min = y
if h - y < min:
    min = h - y
print(min)
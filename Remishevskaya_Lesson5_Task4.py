src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

scr_big = [num for idx, num in enumerate(src) if num > src[idx-1] if idx > 0]

print(scr_big)

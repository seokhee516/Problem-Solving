while True:
    s = input().strip()
    if s == '#':
        break
    cnt = 0
    for c in s:
        if c in 'aeiouAEIOU':
            cnt += 1
    print(cnt)
    
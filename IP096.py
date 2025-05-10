def read():
    global n, h
    n = int(input())
    h = list(map(int, input().split()))
def enlightenment_score(n, h):
    left = [n] * n
    right = [n] * n
    lst = []
    for i in range(n):
        while lst and h[lst[-1]] <= h[i]: lst.pop()
        if lst: left[i] = i - lst[-1]
        lst.append(i)
    lst = []
    for i in range(n - 1, -1, -1):
        while lst and h[lst[-1]] <= h[i]: lst.pop()
        if lst:right[i] = lst[-1] - i
        lst.append(i)
    score = 0
    max_height_index = h.index(max(h))
    for i in range(n):
        if i == max_height_index: continue
        score += min(left[i], right[i])
    print(score)
read()
enlightenment_score(n, h)
def total_sum(n, m):
    total_numbers = n * m
    return total_numbers * (total_numbers + 1) // 2

def vertical_sum(n, m, col):
    return col * n * (col + 1 + m * n - m) // 2

def horizontal_sum(n, m, row):
    return (m * m * row * row + m * row) // 2

def best_vertical(n, m, total):
    lo, hi = 0, m
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if vertical_sum(n, m, mid) <= total // 2:
            lo = mid
        else:
            hi = mid

    best_diff = 10**30
    best_col = 0
    for col in (lo, lo + 1):
        if col < 0 or col > m:
            continue
        s = vertical_sum(n, m, col)
        diff = abs(s - (total - s))
        if diff < best_diff:
            best_diff = diff
            best_col = col
    return best_diff, best_col

def best_horizontal(n, m, total):
    lo, hi = 0, n
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if horizontal_sum(n, m, mid) <= total // 2:
            lo = mid
        else:
            hi = mid

    best_diff = 10**30
    best_row = 0
    for row in (lo, lo + 1):
        if row < 0 or row > n:
            continue
        s = horizontal_sum(n, m, row)
        diff = abs(s - (total - s))
        if diff < best_diff:
            best_diff = diff
            best_row = row
    return best_diff, best_row


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    total = total_sum(n, m)
    diff_v, col = best_vertical(n, m, total)
    diff_h, row = best_horizontal(n, m, total)

    if diff_v <= diff_h:
        print(f"V {col + 1}")
    else:
        print(f"H {row + 1}")

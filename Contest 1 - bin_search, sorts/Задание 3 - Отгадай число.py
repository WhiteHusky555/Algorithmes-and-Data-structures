import sys

def query(x):
    print(x)
    sys.stdout.flush()
    return input()


n = int(input())

flag = False
r = n - 1
l = 0

while r - l > 1:
    m = int((l + r) // 2)
    if query(m) == '>=':
        l = m
    else:
        r = m
print(f"{(l + r) / 2:.6f}")

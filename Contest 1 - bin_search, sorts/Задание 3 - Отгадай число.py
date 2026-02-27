import sys

def query(x):
    print(x, flush=True)
    sys.stdout.flush()
    return input()


n = int(input())

r = n
l = 1
m = 0
while (r - l > 1):
    m = int((l + r) / 2)
    if query(m) == '>=':
        l = m
    else:
        r = m
print(f"!{m}")

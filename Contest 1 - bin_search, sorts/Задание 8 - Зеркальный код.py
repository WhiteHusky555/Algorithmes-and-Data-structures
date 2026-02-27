def count_frequencies(s: str) -> dict[str, int]:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def all_chars_unique(freq: dict[str, int]) -> bool:
    return all(count == 1 for count in freq.values())

def min_odd_char(freq: dict[str, int]) -> str:
    min_char = 'a'
    for ch, count in freq.items():
        if count % 2 != 0:
            min_char = min(min_char, ch)
    return min_char

def build_palindrome(freq: dict[str, int], mid: str) -> str:
    even_chars = []
    for ch in sorted(freq.keys()):
        cnt = freq[ch]
        cnt -= cnt % 2
        even_chars.extend([ch] * cnt)
    total_len = len(even_chars) + (mid != 'a')
    result = [None] * total_len
    i = 0
    even_chars.sort()
    while even_chars:
        result[i] = even_chars.pop(0)
        result[total_len - i - 1] = even_chars.pop(0)
        i += 1
    if mid != 'a':
        result[total_len // 2] = mid
    return ''.join(result)

def algorithm(s: str) -> str:
    s = ''.join(sorted(s))
    freq = count_frequencies(s)
    if all_chars_unique(freq):
        return min(freq.keys())
    mid = min_odd_char(freq)
    return build_palindrome(freq, mid)


n = int(input())
line = input()
result = algorithm(line)
print(result)
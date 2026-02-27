def calculate_total_sum(rows, cols):
    total_elements = rows * cols
    return total_elements * (total_elements + 1) // 2


def calculate_vertical_split_sum(rows, cols, split_col):
    return split_col * rows * (split_col + 1 + rows * cols - rows) // 2


def find_best_vertical_split(rows, cols, total_sum):
    left, right = 0, cols

    while left < right - 1:
        mid = (left + right) // 2
        current_sum = calculate_vertical_split_sum(rows, cols, mid)

        if current_sum <= total_sum // 2:
            left = mid
        else:
            right = mid

    return left, right


def evaluate_vertical_split(rows, cols, split_col, total_sum):
    current_sum = calculate_vertical_split_sum(rows, cols, split_col)
    difference = abs(current_sum - (total_sum - current_sum))
    return difference, split_col, 'V'


def calculate_horizontal_split_sum(rows, cols, split_row):
    return (cols * cols * split_row * split_row + cols * split_row) // 2


def find_best_horizontal_split(rows, cols, total_sum):
    left, right = 0, rows

    while left < right - 1:
        mid = (left + right) // 2
        current_sum = calculate_horizontal_split_sum(rows, cols, mid)

        if current_sum <= total_sum // 2:
            left = mid
        else:
            right = mid

    return left, right


def evaluate_horizontal_split(rows, cols, split_row, total_sum):
    current_sum = calculate_horizontal_split_sum(rows, cols, split_row)
    difference = abs(current_sum - (total_sum - current_sum))
    return difference, split_row, 'H'


def find_optimal_split(rows, cols):
    total_sum = calculate_total_sum(rows, cols)
    best_difference = float('inf')
    best_split_type = 'V'
    best_split_index = 0

    left_split, right_split = find_best_vertical_split(rows, cols, total_sum)

    for split_col in (left_split, right_split):
        if 0 <= split_col <= cols:
            difference, index, split_type = evaluate_vertical_split(rows, cols, split_col, total_sum)
            if difference < best_difference:
                best_difference = difference
                best_split_type = split_type
                best_split_index = index

    top_split, bottom_split = find_best_horizontal_split(rows, cols, total_sum)

    for split_row in (top_split, bottom_split):
        if 0 <= split_row <= rows:
            difference, index, split_type = evaluate_horizontal_split(rows, cols, split_row, total_sum)
            if difference < best_difference:
                best_difference = difference
                best_split_type = split_type
                best_split_index = index

    return best_split_type, best_split_index + 1


def process_test_case():
    rows, cols = map(int, input().split())
    split_type, split_index = find_optimal_split(rows, cols)
    print(f"{split_type} {split_index}")



test_cases = int(input())

for _ in range(test_cases):
    process_test_case()

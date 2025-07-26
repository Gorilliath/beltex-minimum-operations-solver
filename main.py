import argparse
from collections import deque
from operator import add, sub, mul


def min_operations_to_target(target, start_range=range(1, 11), op_range=range(1, 11)):
    # Allowed operations
    operations = [
        (add, "+"),
        (sub, "-"),
        (mul, "*"),
    ]

    # Each state: (current_value, step_count, history)
    queue = deque()
    visited = set()

    # Start with all possible starting numbers (1–10)
    for n in start_range:
        queue.append((n, 0, [str(n)]))
        visited.add(n)

    while queue:
        value, steps, path = queue.popleft()

        if value == target:
            return steps, format_path(path)

        if steps >= 10:
            continue  # Avoid infinite loops or excessive paths

        for op, symbol in operations:
            for n in op_range:
                try:
                    new_val = op(value, n)
                    if new_val < 0 or new_val > target * 2:
                        continue  # Avoid negative or wildly large values
                except:
                    continue  # Skip invalid operations

                if new_val not in visited:
                    visited.add(new_val)
                    queue.append((new_val, steps + 1, path + [f"{symbol}{n}"]))

    return None, "No valid path found"


def format_path(path):
    total = int(path[0])
    parts = [f"{total}"]
    for step in path[1:]:
        op = step[0]
        n = int(step[1:])
        new_total = eval(f"{total}{op}{n}")
        parts.append(f"{total}{op}{n}={new_total}")
        total = new_total
    return " -> ".join(parts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Find the minimum number of sequential arithmetic operations (`+`, `-`, `*`) "
            "to reach a target number using any numbers between `1`–`10`. "
            "Each operation uses the result of the previous step."
        )
    )
    parser.add_argument("target", type=int, help="The target number to reach")

    args = parser.parse_args()
    target = args.target

    steps, sequence = min_operations_to_target(target)
    print(f"Minimum steps: {steps}")
    print(f"Sequence: {sequence}")
